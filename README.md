# Como a Biblioteca funciona?
## Aba ‘Pesquisar Livo’:
![aba_pesquisar](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/a919fc41-f7b5-49da-8a62-145ae3f8cd3b)

### Nessa aba serão apresentados todos os livros cadastrados, seu nome, status(alugado ou não), categoria, autor, se foi emprestado, data de entrega e Id (número identificador). Além disso essa aba também apresenta algumas funcionalidades como ‘Consultar’, ‘Gerar consultas’, ‘Excluir Livro’, ’Pesquisar	‘ e ‘Mostrar Todos’.

### -Consultar:
![aba_consultar](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/7050c6ce-14ab-417e-b3e4-e0392e42687c)

#### Ao selecionar uma tupla(linha) na caixa dos registros listados e clicar em ‘consultar’ uma nova janela será apresentada mostrando os dados da pessoa que alugou aquele livro.

### -Gerar consultas:
![gerar2](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/d54b09f3-1c87-4779-8a67-b0d56b397c81)

#### Ao clicar nesse botão um arquivo de texto será criado e alocado na mesma pasta que o programa está. Esse arquivo de texto contém os dados de todas as pessoas que estão com livros alugados e também diz que livros são esses.

### -Excluir livro:
![excluir](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/86d053f5-d0fe-4aa2-aa3b-bb0221c039da)

#### Ao selecionar uma tupla(linha) na caixa dos registros listados e clicar em ‘Excluir livro’, o livro selecionado será deletado do banco de dados da Biblioteca. Essa função só será possível caso o livro selecionado não esteja alugado

### -Pesquisar:
#### O texto digitado na caixa à esquerda será pesquisado por todos os registros existentes

### -Mostrar Todos:
#### Todos os registros feitos serão listados.

## Aba ‘Cadastrar Livo’:
![aba_cadastro](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/b0aab22b-728d-496b-9446-a40c24230159)

![aba_cadastro2](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/21e40afc-9c3d-4625-a066-9cbb7c44d1a8)

### Nessa aba será feito o cadastro de todos os livros da Biblioteca; o ‘Nome do livro’ deve conter apenas letras, na caixa ‘Selecione a categoria’ inicialmente não apresentará nada, pois nela ficarão todas as categorias que forem cadastradas (para posterior seleção), o campo ‘Autor(a) do livro’ também deve começar com letra maiúscula e conter apenas letras. Uma vez clicado em ‘Cadastrar’ o livro já estará no banco de dados (uma mensagem de sucesso aparecerá para confirmar isso), porém o campo de ‘categoria’ só será atualizado na próxima inicialização do programa. Indo na aba ‘Pesquisasr Livro’ e clicando em ‘Mostrar Todos’ será possível ver os novos registros, porém vale ressaltar que os campos de ‘ID’ das abas ‘Empréstimo’ e ‘Devolução’ também só serão atualizados na próxima inicialização do programa. 

## Aba ‘Empréstimo’:
![aba_emprestar](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/6a78711f-2377-4ca2-9c3c-1f12de7d82ff)

![aba_emprestar2](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/aefa6e99-0253-41eb-96ba-d299b28eddba)

### Nessa aba serão feito os empréstimos dos livros. Todos os campos possuem validação (para que um padrão seja mantido, o que visa facilitar o entendimento) e portanto todos os campos devem seguir essas regras:

### -Nome:
#### Conter apenas letras
	
 ## -CPF:
### Deve estar no padrão: 000.000.000-00, com exatos 11 números, sendo os 6 primeiros separados por um ‘.’ em blocos de 3 números e os 8 últimos separados por ‘-’ em um bloco de três números à esquerda e um bloco de 2 números à direita.
	
 ## -Matrícula:
### conter apenas núemeros
	
## Telefone para contato:
### Conter apenas números, com DD do estado entre parênteses, divido em 2 blocos de números, um com 5 e outro com 4. Ex:(61) 12345-1234; o espaço entre o fechamento do parêntese e início do bloco de números é opcional.

## Aba ‘Devolução’:
![aba_devolucao](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/b19c6d18-f560-476c-8337-eed70845a374)

![aba_devolucao2](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/92b8658d-16e2-4bca-bc71-aac95416018a)

### Nessa aba será feita a devolução dos livros emprestados. Todos os campos também possuem validação (e seguem as mesmas regas dos campos de mesmo nome da aba ‘Empréstimo’), aqui o campo ‘Nome’ deve ser preenchido exatamente da mesma forma que o mesmo campo foi preenchido no empréstimo, assim como o campo ‘CPF’. O ID do livro deve ser consultado na aba ‘Pesquisar Livro’ e pode conter apenas números, após tudo preenchido e validado a devolução é feita e o status do livro deixa de ser ‘Alugado’.

## Campo ‘Menu’:
![menu](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/acd0fd08-42a0-4d06-ac19-172f99ea40dd)

### Esse campo apresenta três funcionalidades: ‘Gerar Banco’,’Zerar Banco’ e ‘Sair’; a opção ‘Sair’ apenas encerra a execução do programa de Biblioteca (porém os dados permanecem salvos, não se preocupe), a opção ‘Gerar Banco’ cria um arquivo de texto com a listagem dos dados de todos os livros já cadastrados na biblioteca e salva esse arquivo na mesma pasta em que o programa se encontra, já a opção ‘Zerar Banco’ deve ser evitada ao máximo e só deve ser usada em situações específicas. O cuidado com essa funcionalidade se faz necessário pois ela vai deletar todos os registros do banco de dados de forma permanente, porém só terá êxito caso não hajam livros emprestados. Caso essa função seja ativada uma pasta de backup será criada dentro do mesmo diretório que esse programa se encontra, dentro dessa nova pasta será criado um arquivo de texto com todos os registros que tinham na biblioteca antes da deleção total dos dados.

### Sair:
![sair](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/bd9bc916-7fcc-4559-a69e-01aa94d8465c)

### Zerar Banco: 
![zerar](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/d8b6ebae-5909-424b-9320-83d0e48f8d86)

### Gerar Banco:
![gerar](https://github.com/Gustavo-erades/Biblioteca/assets/108373134/42124d39-8823-4142-a593-ab24c5208d08)

## Um pouco mais sobre o programa:
#### *Os Ids são gerados automáticamente, o próprio programa escolhe números aleatórios numa faixa de de 100 a 10000, esse sistema foi feito para facilitar o cadastro dos livros, pois você, como usuário, não precisa se preocupar com os ids. Porém, caso queira personalizar os ids para melhorar sua organização é possível. Basta, ao cadastrar o livro, alterar o campo de 'id do livro'; OBS: os ids podem ter até 5 caracteres e podem conter tanto letras quanto números.

#### *O campo de CPF e de Matrícula têm a mesma função (servir de identificador para quem alugou o livro) e por isso caso um esteja preenchido, preencher o outro se torna opcional. O campo de CPF precisa estar no padrão 000.000.000-00, mas a única restrição que o campo de matrícula tem é de poder conter apenas números.

#### *Os campos de datas podem usar como separador a '/' ou '-', ambos podem ser usados para separara dia, mês e ano.

### *O arquivo "Biblioteca.rar" possui uma pasta compactada com um executável do programa para que ele possa ser utilizado.

#### *A pasta desse programa é necessária para seu pleno funcionamento, portanto você NÃO deve retirá-la do seu computador. Essa pasta também servirá como base para o programa. O que significa que quando for necessário gerar uma pasta de backup ou um arquivo txt qualquer, a pasta de destino será a mesma de origem desse programa. Mas, fique a vontade para alocar essa pasta onde preferir ou criar um atalho desse programa. OBS: caso queira abrir o programa clicando em seu ícone porém fora da pasta de origem, crie um atalho e o aloque onde preferir. 

