Comandos do programa:
      "GET [1]": "/books                      -->  lista todos os livros lançados até o momento",
      "GET [2]": "/books/{id}                 -->  fornece informações sobre um livro específico",
      "GET [3]": "/authors                    -->  lista todos os autores lançados até o momento",
      "GET [4]": "/authors/{id}               -->  fornece informações sobre um autor específico",
      "GET [5]": "/authors/{id}/books         -->  lista todos os livros com o 'autor_id' daquele autor",
      "POST [1]": "/books                     -->  lança um livro novo",
      "POST [2]": "/authors                   -->  lança um autor novo",
      "POST [3]": "/authors/{id}/books/{id}   -->  associa um autor a um livro",
      "PUT [1]": "/books/{id}                 -->  permite a edição das informações de um livro",
      "PUT [2]": "/authors/{id}               -->  permite a edição das informações de um autor",
      "DELETE [1]": "/books/{id}              -->  deleta um livro específico",
      "DELETE [2]": "/authors/{id}            -->  deleta um autor específico",
      "DELETE [3]": "/authors/{id}/books/{id} -->  remove a associação entre um autor e um livro"
                    
