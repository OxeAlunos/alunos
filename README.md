# alunos
Projeto em conjunto

## Observações

Todos os desafios ou programação são utilizados apenas como um meio de desafiar e ajudar os alunos a fixarem conteúdos e verem na prática como aplicamos os mesmos.
Não sendo obrigátorio a execução dos mesmos.


## Dúvidas

No caso de dúvida sobre testar os métodos POST e PUT não é necessário ter pressa, são assuntos que ainda estão pendentes. Podemos resolvê-los conforme as aulas.



## No que eu devo focar no momento? 29/06 - 04/07

- As classes, fiz todas as classes? Determinei seus métodos e atributos da maneira correta?

- Os GETs, fiz as rotas GETs necessárias? Quais faltam?



## Funcionalidades que deve possuir:

*  Gerenciamento de Livros
    
    * Listar os livros
        * Tem que possuir a rota get /livros que retorna um array com todos os livros
    * Listar livros pelo autor
        * GET - /livro/autor?
    * Listar livros pelo nome
        * GET - /livro/nome?
    * Listar livros pelo ISBN
        * GET - /livro/isbn?
    * Referência para Get com paramêtros:
        https://fastapi.tiangolo.com/pt/tutorial/query-params/
    * Adicionar um livro
        * Tem que possuir a rota post /livro que deve receber um livro e salva-lo no banco de dados
    * Atualizar dados de um livro
        * PUT - /livro/{ id } 
    * Deletar dados de um livro
        * DELETE - /livro/{ id }

* Gerenciamento de Usuários/Leitores/Adm
    
    * Listar leitores
        * GET - /usuarios
    * Listar um usuário
        * GET - /usuario/{ id }
    * Adicionar um leitor
        * POST - /usuario
    * Atualizar dados de um leitor
        * PUT - /usuario
    * Deletar leitor
        * DELETE - /usuario/{ id }


* Guardar os dados em um "banco" que no nosso exemplo será o excel
    * Deve-se usar o pandas
    * Criar uma classe chamada BancoDeDados
        * Terá somente metódos
        * Esses metodos devem salvar no excel tudo que for criado

* Desafios extras
    * O sistema deve carregar os dados salvos no excel quando ele for executado.
    * Quem é interessado para criar uma rota que devolve um pdf com relatórios de quantidade de livros por genêro?
        * Para isso terá que pesquisar sobre bibliotecas para criar PDF + Relatórios.
        * Ex: Matplotlib para graficos/relatórios.
        * FPDF para criar pdfs.