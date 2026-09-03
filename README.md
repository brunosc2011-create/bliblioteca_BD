# bliblioteca_BD - Aplicação com Banco de dados

implementação do exemplo da biblioteca salvando os dados em um banco de dados *SQlite*

usuarios ( id, nome )
autores ( id, nome )
editoras ( id, nome )
livros ( id, titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel )
emprestimos ( id, usuario_id, data )
emprestimos_livros ( emprestimo_id, livro_id, data_devolucao )