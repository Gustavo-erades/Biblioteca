--- Como a Biblioteca funciona? ---

Aba ‘Pesquisar Livo’:
	Nessa aba serão apresentados todos os livros cadastrados, seu nome, status(alugado ou não), categoria, autor, se foi emprestado, data de entrega e Id (número identificador).
	Além disso essa aba também apresenta algumas funcionalidades como ‘Consultar’, ‘Gerar consultas’, ‘Excluir Livro’, ’Pesquisar	‘ e ‘Mostrar Todos’.

-Consultar:
	Ao selecionar uma tupla(linha) na caixa dos registros listados e clicar em ‘consultar’ uma nova janela será apresentada mostrando os dados da pessoa que alugou aquele livro.

-Gerar consultas:
	Ao clicar nesse botão um arquivo de texto será criado e alocado na mesma pasta que o programa está. Esse arquivo de texto contém os dados de todas as pessoas que estão com livros alugados e também diz que livros são esses.

-Excluir livro:
	Ao selecionar uma tupla(linha) na caixa dos registros listados e clicar em ‘Excluir livro’, o livro selecionado será deletado do banco de dados da Biblioteca. Essa função só será possível caso o livro selecionado não esteja alugado

-Pesquisar:
	O texto digitado na caixa à esquerda será pesquisado por todos os registros existentes

-Mostrar Todos:
	Todos os registros feitos serão listados.
------------------------------------------------------------------

Aba ‘Cadastrar Livo’:
	Nessa aba será feito o cadastro de todos os livros da Biblioteca; o ‘Nome do livro’ deve começar com letra maiúscula e conter apenas letras, na caixa ‘Selecione a categoria’ inicialmente não apresentará nada, pois nela ficarão todas as categorias que forem cadastradas (para posterior seleção), o campo ‘Autor(a) do livro’ também deve começar com letra maiúscula e conter apenas letras.
	Uma vez clicado em ‘Cadastrar’ o livro já estará no banco de dados (uma mensagem de sucesso aparecerá para confirmar isso), porém o campo de ‘categoria’ só será atualizado na próxima inicialização do programa. Indo na aba ‘Pesquisasr Livro’ e clicando em ‘Mostrar Todos’ será possível ver os novos registros, porém vale ressaltar que os campos de ‘ID’ das abas ‘Empréstimo’ e ‘Devolução’ também só serão atualizados na próxima inicialização do programa. 
------------------------------------------------------------------

Aba ‘Empréstimo’:
	Nessa aba serão feito os empréstimos dos livros. Todos os campos possuem validação (para que um padrão seja mantido, o que visa facilitar o entendimento) e portanto todos os campos devem seguir essas regras:
	-Nome:
		Começa com letra maiúscula e contém apenas letras
	-CPF:
		Deve estar no padrão: 000.000.000-00, com exatos 11 números, sendo os 6 primeiros separados por um ‘.’ em blocos de 3 números e os 8 últimos separados por ‘-’ em um bloco de três números à esquerda e um bloco de 2 números à direita.
	-Telefone para contato:
		Conter apenas números, com DD do estado entre parênteses, divido em 2 blocos de números, um com 5 e outro com 4. Ex:(61) 12345-1234; o espaço entre o fechamento do parêntese e início do bloco de números é opcional.
------------------------------------------------------------------

Aba ‘Devolução’:
	Nessa aba será feita a devolução dos livros emprestados. Todos os campos também possuem validação (e seguem as mesmas regas dos campos de mesmo nome da aba ‘Empréstimo’), aqui o campo ‘Nome’ deve ser preenchido exatamente da mesma forma que o mesmo campo foi preenchido no empréstimo, assim como o campo ‘CPF’. O ID do livro deve ser consultado na aba ‘Pesquisar Livro’ e pode conter apenas números, após tudo preenchido e validado a devolução é feita e o status do livro deixa de ser ‘Alugado’.
------------------------------------------------------------------
Campo ‘Menu’:
	Esse campo apresenta três funcionalidades: ‘Gerar Banco’,’Zerar Banco’ e ‘Sair’; a opção ‘Sair’ apenas encerra a execução do programa de Biblioteca (porém os dados permanecem salvos, não se preocupe), a opção ‘Gerar Banco’ cria um arquivo de texto com a listagem dos dados de todos os livros já cadastrados na biblioteca e salva esse arquivo na mesma pasta em que o programa se encontra, já a opção ‘Zerar Banco’ deve ser evitada ao máximo e só deve ser usada em situações específicas. O cuidado com essa funcionalidade se faz necessário pois ela vai deletar todos os registros do banco de dados de forma permanente, porém só terá êxito caso não hajam livros emprestados. Caso essa função seja ativada uma pasta de backup será criada dentro do mesmo diretório que esse programa se encontra, dentro dessa nova pasta será criado um arquivo de texto com todos os registros que tinham na biblioteca antes da deleção total dos dados.
