from http.server import BaseHTTPRequestHandler, HTTPServer
import json

#   Criando o nosso armazenamento dos livros e autores criados no formato de dicionário:
livros = {}
autores = {}
#   Criando nossa estratégia para gerar id's diferentes automaticamente para cada livro e autor:
proximo_id_livro = 1
proximo_id_autor = 1

#   Criando a classe BibliotecaApi que herda do BaseHTTPRequestHandler
class BibliotecaApi(BaseHTTPRequestHandler):

 #   Função para construir e enviar a resposta HTTP pro cliente após processar cada requisição:
    def enviar_resposta(self, status_code, conteudo=None):
 #   Usaremos o "self." para conseguirmos acessar toda a class.
 #       Definindo o código de status:
        self.send_response(status_code) 
 #       OBS: 200 = OK, 404 = Not Found, 201 = Created, 400 = Bad Request

 #       Definindo o tipo de conteúdo:
        self.send_header("Content-type", "application/json")

 #       Finalizando o cabeçário e preparando o servidor para enviar o corpo da resposta
        self.end_headers()

 #       Se houver conteúdo para ser enviado...
 #       Enviando o conteúdo da resposta (convertido para JSON e codificado em bytes para ser enviado pelo método self.wfile.write())
        if conteudo:
            self.wfile.write(json.dumps(conteudo).encode('utf-8'))

 #   Para facilitar, todas as funções GET serão definidas ao mesmo tempo
    def do_GET(self):
 #       Se não recebeu nenhuma entrada
        if not self.path:
            self.enviar_resposta(404, {"Erro 404": "Nenhum comando GET com esse caminho existe, use /rotas para visualizar todos os comandos"})
            return

 #       Salvando o caminho em uma lista de strings, para acessar os diferentes elementos do caminho a depender da situação
        caminho = self.path.split("/")
 #       Lembrete: (caminho[0] = "")

 #       Caminho * GET /books * (listar todos os livros)
 #       Se o primeiro elemento do caminho for "books" e não tiver nenhum id
        if caminho[1] == "books" and len(caminho) == 2:             
            self.enviar_resposta(200, list(livros.values()))

 #       Caminho * GET /books/{id} * (obter detalhes de um livro com id {id})
 #       Se o primeiro elemento do caminho for "books" e tiver um id
        elif caminho[1] == "books" and len(caminho) == 3:           
            id = int(caminho[2])                                     # Transforma em valor numero a {id}, pois todas as ID's são int, já que criamos um contador nas linhas 8,9
            
            if id in livros:
                self.enviar_resposta(200, livros[id])
            else:
                self.enviar_resposta(404, {"Erro 404": "Ooops! Nenhum livro com esse id foi encontrado! ☹"})

 #       Caminho * GET /authors *  (listar todos os autores)
 #       Se o primeiro elemento do caminho for "authors" e não tiver nenhum id
        elif caminho[1] == "authors" and len(caminho) == 2:          # Esse len(caminho) == 2 é porque caminho = ['', 'authors']
            self.enviar_resposta(200, list(autores.values()))

 #       Caminho * GET /authors/{id} * (obter detalhes de um autor específico)
 #       Se o primeiro elemento do caminho for "authors" e tiver um id
        elif caminho[1] == "authors" and len(caminho) == 3:          # Esse len(caminho) == 3 é porque caminho = ['', 'authros', '{id}']
            id = int(caminho[2])                                     # Transforma em valor numero a {id}, pois todas as ID's são int, já que criamos um contador nas linhas 8,9
            if id in autores:
                self.enviar_resposta(200, autores[id])
            else:
                self.enviar_resposta(404, {"Erro 404": "Ooops! Nenhum autor com esse id foi encontrado! ☹"})

 #       Caminho * GET /authors /{id} /books * (listar os livros de um autor)
 #       Se o primeiro elemento for authors e tiver além de um id, a string books
        elif caminho[1] == "authors" and len(caminho) == 4:         
            id = int(caminho[2])                                     # Transforma em valor numero a {id}, pois todas as ID's são int, já que criamos um contador nas linhas 8,9
            if id in autores:         
                livros_do_autor = []                                 # Cria uma lista vazia para adicionarmos todos os livros com o mesmo "autor_id" que recebem1os

                for livro in livros:
                    if str(livros[livro].get("autor_id")) == str(id):
                        livros_do_autor.append([f"titulo = {livros[livro].get("titulo")}", f"id = {livros[livro].get("id")}"])
                
                self.enviar_resposta(200, livros_do_autor)          # "Printa" todas os livro
            
            else:
                self.enviar_resposta(404, {"Erro 404": "Ooops! Nenhum autor com esse id foi encontrado! ☹"})    # Caso 
        
 #       Função que mostra todas as rotas
 #       GET /rotas
        elif len(caminho) > 1 and caminho[1] == "rotas":
            if len(caminho) == 2:                             
                rotas = {
                    "GET [1]": "/books                      -->  Lista todos os livros lançados até o momento",
                    "GET [2]": "/books/{id}                 -->  Fornece informações sobre um livro específico",
                    "GET [3]": "/authors                    -->  Lista todos os autores lançados até o momento",
                    "GET [4]": "/authors/{id}               -->  Fornece informações sobre um autor específico",
                    "GET [5]": "/authors/{id}/books         -->  Lista todos os livros com o 'autor_id' daquele autor",
                    "POST [1]": "/books                     -->  Lança um livro novo",
                    "POST [2]": "/authors                   -->  Lança um autor novo",
                    "POST [3]": "/authors/{id}/books/{id}   -->  Associa um autor a um livro",
                    "PUT [1]": "/books/{id}                 -->  Permite a edição das informações de um livro",
                    "PUT [2]": "/authors/{id}               -->  Permite a edição das informações de um autor",
                    "DELETE [1]": "/books/{id}              -->  Deleta um livro específico",
                    "DELETE [2]": "/authors/{id}            -->  Deleta um autor específico",
                    "DELETE [3]": "/authors/{id}/books/{id} -->  Remove a associação entre um autor e um livro"
                }

                self.enviar_resposta(200, rotas)

 #           Sequência de condicionais para mostrar rotas de um determinado tipo específico
            elif len(caminho) > 2:                              
                if caminho[2] == "get":
                    rotas = {
                        "GET [1]": "/books                      -->  lista todos os livros lançados até o momento",
                        "GET [2]": "/books/{id}                 -->  fornece informações sobre um livro específico",
                        "GET [3]": "/authors                    -->  lista todos os autores lançados até o momento",
                        "GET [4]": "/authors/{id}               -->  fornece informações sobre um autor específico",
                        "GET [5]": "/authors/{id}/books         -->  lista todos os livros com o 'autor_id' daquele autor"
                    }

                    self.enviar_resposta(200, rotas)

                elif caminho[2] == "post" and len(caminho) == 3:
                    rotas = {
                        "POST [1]": "/books                     -->  lança um livro novo",
                        "POST [2]": "/authors                   -->  lança um autor novo",
                        "POST [3]": "/authors/{id}/books/{id}   -->  associa um autor a um livro",
                        "Mais informações": "/?"
                    }

                    self.enviar_resposta(200, rotas)

                elif caminho[2] == "post" and len(caminho) == 4 and caminho[3] == "?":
                    tutorial = {
                        "Exemplo de livro": {
                            "id": "  *gerado automaticamente*  ",
                            "titulo": "  *obrigatório*  ",
                            "genero": "  *opcional*  ",
                            "ano": "  *opcional*  ",
                            "autor_id": "  *opcional*  "
                        },

                        "Exemplo de autor": {
                            "id": "  *gerado automaticamente*  ",
                            "nome": "  *obrigatório*  ",
                            "data_nascimento": "  *opcional*  ",
                            "nacionalidade": "  *opcional*  "
                        },

                        "Observação": "Caso alguma informação opcional não seja fornecida, será registrado 'Desconhecido'. "
                    }

                    self.enviar_resposta(200, tutorial)

                elif caminho[2] == "put" and len(caminho) == 3:
                    rotas = {
                        "PUT [1]": "/books/{id}                 -->  permite a edição das informações de um livro",
                        "PUT [2]": "/authors/{id}               -->  permite a edição das informações de um autor",
                        "Mais informações": "/?"
                    }

                    self.enviar_resposta(200, rotas)
                
                elif caminho[2] == "put" and len(caminho) == 4 and caminho[3] == "?":
                    tutorial = {
                        "Exemplo de livro": {
                            "id": "  *imutável*  ",
                            "titulo": "  Novo Título Exemplo  ",
                            "genero": "  Novo Gênero Exemplo  ",
                            "ano": "  Novo Ano Exemplo  ",
                            "autor_id": "  Novo Autor_id Exemplo  "
                        },

                        "Exemplo de autor": {
                            "id": "  *imutável*  ",
                            "nome": "  Novo Nome Exemplo  ",
                            "data_nascimento": "  Nova Data de Nascimento Exemplo  ",
                            "nacionalidade": "  Nova Nacionalidade Exemplo  "
                        },

                        "Observação": """Caso não deseje-se alterar alguma informação, a linha inteira daquela informação deverá ser excluída,
                        caso apenas a parte à direita do ':' seja excluída, será registrado 'Desconhecido'. """
                    }

                    self.enviar_resposta(200, tutorial)


                elif caminho[2] == "delete":
                    rotas = {
                        "DELETE [1]": "/books/{id}              -->  deleta um livro específico",
                        "DELETE [2]": "/authors/{id}            -->  deleta um autor específico",
                        "DELETE [3]": "/authors/{id}/books/{id} -->  remove a associação entre um autor e um livro"
                    }

                    self.enviar_resposta(200, rotas)
                
                else:
                    self.enviar_resposta(400, {"Erro 400": "Tipo de rota não encontrado"})

        else:
            self.enviar_resposta(404, {"Erro 404": "Nenhum comando GET com esse caminho existe, use /rotas para visualizar todos os comandos"})



 #       Fim das funções GET...
    
    def do_POST(self):
        
        global proximo_id_livro
        global proximo_id_autor

        # Novamente, salvando o caminho em uma lista de strings:
        caminho = self.path.split('/')


        # POST /books: criar um novo livro
        # Se o primeiro elemento do caminho for books
        if caminho[1] == "books":
            # Pegando o tamanho do conteúdo que será passado para a api
            conteudo_tamanho = self.get_content_length()

            

            # O corpo do conteúdo que será enviado é lido de acordo com o tamanho que foi passado,
            # e como esse conteúdo está em bytes, é necessário decodificá-lo em uma string legível
            corpo = self.rfile.read(conteudo_tamanho).decode('utf-8')

            # Transformando os dados em JSON para um dicionário em python e armazenando na variável "dados"
            dados = json.loads(corpo)

            if not conteudo_tamanho:
                self.enviar_resposta(404, {"Erro": "O tamanho do conteúdo não está especificado."})
                return
        
            # Criando um novo livro com um determinado id
            novo_livro = {
                "id": proximo_id_livro,
                "titulo": dados.get("titulo", "Desconhecido"),
                "genero": dados.get("genero", "Desconhecido"),
                "ano": dados.get("ano", "Desconhecido"),
                "autor_id": dados.get("autor_id", "Desconhecido"),
            }

            if novo_livro["titulo"] == "Desconhecido":
                self.enviar_resposta(400, {"Erro 400": "É obrigatório inserir o nome do livro para adiciona-lo"})
                return
            
            if novo_livro["autor_id"] != "Desconhecido":
                if novo_livro["autor_id"] not in autores:
                    novo_livro["autor_id"] = "Desconhecido"
                    self.enviar_resposta(200, {"Sucesso" : "Id do Autor não encontrado, substituido por Desconhecido"})

            livros[proximo_id_livro] = novo_livro

            # Incrementando o proximo_id_livro para que na próxima vez que essa condicional seja acessada, o id do livro seja único
            proximo_id_livro += 1

            self.enviar_resposta(200, novo_livro)
        # POST /authors: criar um novo autor
        # Se o primeiro elemento do caminho for authors e não houver um id depois
        elif caminho[1] == "authors" and len(caminho) == 2:
            # Pegando o tamanho do conteúdo que será passado para a api
            conteudo_tamanho = self.get_content_length()

            

            # O corpo do conteúdo que será enviado é lido de acordo com o tamanho que foi passado,
            # e como esse conteúdo está em bytes, é necessário decodificá-lo em uma string legível
            corpo = self.rfile.read(conteudo_tamanho).decode('utf-8')

            # Transformando os dados em JSON para um dicionário em python e armazenando na variável "dados"
            dados = json.loads(corpo)
            
            if not conteudo_tamanho:
                self.enviar_resposta(404, {"Erro": "O tamanho do conteúdo não está especificado."})
                return
            
            # Lógica análoga à função anterior
            novo_autor = {
                "id": proximo_id_autor,
                "nome": dados.get("nome", "Desconhecido"),
                "data_nascimento": dados.get("data_nascimento", "Desconhecido"),
                "nacionalidade": dados.get("nacionalidade", "Desconhecido"),
            }

            if novo_autor["nome"] == "Desconhecido":
                self.enviar_resposta(400, {"Erro 400": "É obrigatório inserir o nome do autor para adiciona-lo"})
                return
            
            autores[proximo_id_autor] = novo_autor
            proximo_id_autor += 1

            self.enviar_resposta(201, novo_autor)


        # POST /authors/{id}/books/{id}: associar um livro a um autor
        # Se o primeiro elemento do caminho for authors e houver um id, books e outro id 
        elif caminho[1] == "authors" and caminho[3] == "books" and len(caminho) == 5:
            id_autor = int(caminho[2])
            id_livro = int(caminho[4])

            if id_autor in autores and id_livro in livros:
                livros[id_livro]["autor_id"] = id_autor
                self.enviar_resposta(200, {"Sucesso": "O autor foi associado ao livro"})

            elif id_autor in autores and not id_livro in livros:
                self.enviar_resposta(404, {"Erro 404": "Ooops! Nenhum livro com esse id foi encontrado! ☹"})

            elif not id_autor in autores:
                self.enviar_resposta(404, {"Erro 404": "Ooops! Nenhum autor com esse id foi encontrado! ☹"})

        else:
            self.enviar_resposta(404, {"Erro": "Nenhum comando POST com esse caminho existe, use /rotas para visualizar todos os comandos"})

        # Fim das funções POST...

    # Função auxiliar para pegar o tamanho do conteúdo
    def get_content_length(self):
        if self.headers.get('Content-Length'):
            return int(self.headers.get('Content-Length'))
        return
        
    def do_PUT(self):
        caminho = self.path.split('/')
        conteudo_tamanho = self.get_content_length()

        if not conteudo_tamanho:
            self.enviar_resposta(404, {"Erro": "O tamanho do conteúdo não está especificado."})
            return

        corpo = self.rfile.read(conteudo_tamanho).decode('utf-8')
        dados = json.loads(corpo)

        if len(caminho) != 3:
            self.enviar_resposta(404, {"Erro" : "Caminho inválido. Use /books/{id} ou /authors/{id}."})
            return

        id = int(caminho[2])  # Transformar o id

        if caminho[1] == "books":
            
            dados = {
                "titulo": dados.get("titulo", "Desconhecido"),
                "genero": dados.get("genero", "Desconhecido"),
                "ano": dados.get("ano", "Desconhecido")
            }

            if dados.get("titulo") == "Desconhecido":
                dados["titulo"] = livros[id]["titulo"]

            if dados.get("genero") == "Desconhecido":
                dados["genero"] = livros[id]["genero"]

            if dados.get("ano") == "Desconhecido":
                dados["ano"] = livros[id]["ano"]

            if id in livros:
                livros[id].update(dados)
                self.enviar_resposta(200, livros[id])
            else:
                self.enviar_resposta(404, {"Erro 404": "Ooops! Nenhum livro com esse id foi encontrado! ☹"})

        elif caminho[1] == "authors":

            dados = {
                "nome": dados.get("nome", "Desconhecido"),
                "data_nascimento": dados.get("data_nascimento", "Desconhecido"),
                "nacionalidade": dados.get("nacionalidade", "Desconhecido"),
                }
            
            if dados.get("nome") == "Desconhecido":
                dados["nome"] = autores[id]["nome"]

            if dados.get("data_nascimento") == "Desconhecido":
                dados["data_nascimento"] = autores[id]["data_nascimento"]

            if dados.get("nacionalidade") == "Desconhecido":
                dados["nacionalidade"] = autores[id]["nacionalidade"]
                

            if "id" in dados:
                self.enviar_resposta(404, {"Erro" : "Não é possível alterar a id"})
                dados["id"] = autores[id]["id"]

            if id in autores:
                autores[id].update(dados)
                self.enviar_resposta(200, autores[id])
            else:
                self.enviar_resposta(404, {"Erro 404": "Ooops! Nenhum autor com esse id foi encontrado! ☹"})

        else:
            self.enviar_resposta(404, {"Erro 404": "Caminho inválido. Use /books/{id} ou /authors/{id}."})


    def do_DELETE(self):
        #Funções
            # DELETE books/id: excluir um livro
            # DELETE /authors/id: excluir um autor
            # DELETE /authors/id/books/id: remover a associação entre um autor e um livro
            # Fim das funções PUT...

        caminho = self.path.split('/')

        #Confere se o tamanho do caminho são 2 endereçamentos
        if len(caminho) == 3:

            #Salva o ID
            id = int(caminho[2])

            #Confere se o ID digitado é válido
            if id in livros or id in autores:

                #Caso queira mexer nos livros    
                if caminho[1] == "books":
                    del livros[id]
                    self.enviar_resposta(200, {"Sucesso" : "Livro excluido com sucesso!"})

                #Caso queira mexer nos autores
                elif caminho[1] == "authors":
                    del autores[id]
                    self.enviar_resposta(200, {"Sucesso" : "Autor excluido com sucesso!"})
            
            #Caso o caminho esteja errado
            else:
                self.enviar_resposta(404, {"Erro 404": "Ooops! Nenhum livro ou autor com esse id foi encontrado! ☹"})

        #Caso queira desassociar um autor de um livro
        elif caminho[1] == "authors" and caminho[3] == "books":

            #Salva os ID's
            id_autor = int(caminho[2])
            id_livro = int(caminho[4])

            #Se os ID's são válidos
            if id_autor in autores and id_livro in livros:
                livros[id_livro]["autor_id"] = "Desconhecido"
                self.enviar_resposta(200, {"Sucesso" : "Autor não está mais associado ao livro"})
            #ID's não válidos
            else:
                self.enviar_resposta(404, {"Erro 404": "Digite correntamente os ID's!"})

        else:
            self.enviar_resposta(404, {"Erro": "Nenhum comando DELETE com esse caminho existe, use /rotas para visualizar todos os comandos"})

def run():
    servidor = HTTPServer(('localhost', 8080), BibliotecaApi)
    print("Servidor iniciado na porta 8080...")
    servidor.serve_forever()

run()

###### ULTIMA VERSÃO DA BIBLIOTECA_API 
###### TUDO FINALIZADO