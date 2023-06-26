#importa as bibliotecas para gui e banco de dados
import tkinter as tk
from tkinter import ttk
import sqlite3 as conector
from tkinter import messagebox as mb
import os
from random import *
import banco
import regex_biblioteca
#abre o banco de dados e cria as tabelas
try:
    pastaApp=os.path.dirname(__file__)
    tabela_livro='''CREATE TABLE IF NOT EXISTS Livro(
                    nome TEXT NOT NULL,
                    status TEXT,
                    categoria TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    data_alug TEXT,
                    data_entrega TEXT,
                    id INTEGER NOT NULL,
                    PRIMARY KEY(id)
                    );'''
    tabela_pessoa='''CREATE TABLE IF NOT EXISTS Pessoa(
                    cpf TEXT NOT NULL,
                    id_livro TEXT NOT NULL,
                    nome TEXT NOT NULL,
                    contato TEXT NOT NULL,
                    PRIMARY KEY(cpf),
                    FOREIGN KEY (id_livro) REFERENCES Livro(id)
                    );'''
    banco.dml(tabela_livro)
    banco.dml(tabela_pessoa)
    def centralizar_janela(nomeDaJanela,valorLargura,valorAltura):
        largura=valorLargura
        altura=valorAltura
        largura_screen=nomeDaJanela.winfo_screenwidth()
        altura_screen=nomeDaJanela.winfo_screenheight()
        posx=  (largura_screen/2)-(largura/2)
        posy= (altura_screen/2)-(altura/2)
        nomeDaJanela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))
        nomeDaJanela.resizable(False,False)
    def semComando():
        print("sem comando")
    def refresh():
        tk.mainloop()
    def verificacao_sair():
        if mb.askyesno("Verificação", "Deseja realmente sair?"):
            janela.quit()
        else:
            mb.showerror("Verificação","Opção de saída cancelada")
    def verificacao_deletar():
        if mb.askyesno("Verificar deleção","Deseja realmente deletar esse livro?"):
            print("Ainda sem comando :(")
            mb.showinfo("Sucesso :)","Livro deletado da biblioteca!")
        else:
            mb.showerror("Erro :(","Deleção cancelada!")
    #conteúdo das abas
    def popularGrid():
        tv.delete(*tv.get_children())
        vquery="SELECT * FROM Livro ORDER BY id"
        linhas=banco.dql(vquery)
        for i in linhas:
            tv.insert("","end",values=i)
    def procurar():
        tv.delete(*tv.get_children())
        vquery="SELECT * FROM Livro WHERE (nome LIKE '%"+str(pesquisar.get())+"%') OR (status LIKE '%"+str(pesquisar.get())+"%') OR (categoria LIKE '%"+str(pesquisar.get())+"%') OR (autor LIKE '%"+str(pesquisar.get())+"%') OR (data_alug LIKE '%"+str(pesquisar.get())+"%') OR (data_entrega LIKE '%"+str(pesquisar.get())+"%') OR (id LIKE '%"+str(pesquisar.get())+"%') ORDER BY id"
        linhas=banco.dql(vquery)
        for i in linhas:
            tv.insert("","end",values=i)
    val=randint(100,1000)
    def cont_abaCadastro():
        if (Nome.get()!="" and categoria.get()!="" and autor.get()!=""):
            if(regex_biblioteca.validanome(Nome.get()) and regex_biblioteca.validanome(autor.get())):
                vnome=str(Nome.get())
                vcategoria=str(categoria.get())
                vautor=str(autor.get())
                vquery="INSERT INTO Livro(nome,categoria,autor,id) VALUES('"+vnome+"','"+vcategoria+"','"+vautor+"','"+str(val)+"');"
                banco.dml(vquery)
                mb.showinfo("Sucesso :)","Livro cadastrado com sucesso!\n\n*OBS: caso tenha sido cadastrado uma nova categoria ela estará disponível na próxima inicialização do programa, assim como o número ID do livro cadastrado.*")
            else:
                mb.showwarning("ATENÇÃO","Os campos de 'Nome do livro' e 'Nome do autor(a)' devem começar com letra Maiúscula")
        else:
            mb.showerror("Erro :(","Todos os campos devem ser preenchidos!")
    def cont_abaEmprestar():
        if (Nome_pessoa.get()!="" and cpf_pessoa.get()!="" and contato_pessoa.get()!="" 
            and ID_livro.get()!="" and data_emprestimo.get()!="" and data_entrega.get()!=""):
            if(regex_biblioteca.validatelefone(contato_pessoa.get()) and regex_biblioteca.validacpf(cpf_pessoa.get()) and 
               regex_biblioteca.validanome(Nome_pessoa.get()) and regex_biblioteca.validaid(ID_livro.get()) and 
               regex_biblioteca.validadata(data_emprestimo.get()) and regex_biblioteca.validadata(data_entrega.get())):
                comando="SELECT nome FROM Livro WHERE id='"+str(ID_livro.get())+"';"
                if(banco.dql(comando)):
                    #pega nome, cpf e contato da pessoa
                    vnome=str(Nome_pessoa.get())
                    vcpf=str(cpf_pessoa.get())
                    vcontato=str(contato_pessoa.get())
                    vid_livro=str(ID_livro.get())
                    vdata_emprestimo=str(data_emprestimo.get())
                    vdata_entrega=str(data_entrega.get())
                    vquery="INSERT INTO Pessoa(cpf,id_livro,nome,contato) VALUES('"+vcpf+"','"+vid_livro+"','"+vnome+"','"+vcontato+"');"
                    banco.dml(vquery)
                    #atualiza status do livro emprestado
                    atualiza_status="UPDATE Livro SET status='Alugado', data_alug='"+vdata_emprestimo+"', data_entrega='"+vdata_entrega+"' WHERE id='"+vid_livro+"';"
                    banco.dml(atualiza_status)
                    mb.showinfo("Sucesso :)","%s tem até %s para entregar o livro!"%(vnome,vdata_entrega))
                else:
                    mb.showerror("ERRO :(","O livro de id: '"+str(ID_livro.get())+"' não existe!")
            else:
                mb.showwarning("ATENÇÃO","O campos devem ser preenchidos da seguinte forma:\n*Nome começando com Letra maiúscula*\n*CPF: 000.000.000-00*\n*Contato:(99) 99999-9999\n*Id até cinco caracteres, contendo letras ou números*\n*Data: 00/00/0000 ou 00-00-0000")
        else:
            mb.showerror("ERRO :(","Todos os campos devem ser preenchidos!")
    def zera_banco():
        if(mb.askyesno("ATENÇÃO","Ao zerar o banco todos os dados de livros cadastrados e de empréstimos feitos serão perdidos! Deseja realmente zerar o banco?")):
            comando_garantia="SELECT * FROM Livro WHERE status='Alugado'"
            garantia=banco.dml(comando_garantia)
            if garantia==[] or garantia==None:
                os.mkdir(pastaApp+"\\Biblioteca_backup")
                comando_sensatoLivro="SELECT * FROM Livro ORDER BY ID"
                resultado_sensatoLivro=banco.dql(comando_sensatoLivro)
                if(resultado_sensatoLivro!=[]):   
                    with open(""+pastaApp+"\\Biblioteca_backup\\backup_Livros_Registrados.txt","w",encoding="UTF-8") as f:
                            f.write("\t--- BACKUP DOS LIVROS CADASTRADOS ---\n\n")
                            for i in resultado_sensatoLivro:
                                lista_populaArq=(i)
                                f.write("Livro: %s | Autor: %s | Categoria: %s | ID: %s\n"%(lista_populaArq[0],lista_populaArq[3],lista_populaArq[2],lista_populaArq[6]))
                    comando_insanidade1="DELETE FROM Pessoa"
                    banco.dml(comando_insanidade1)
                    comando_insanidade2="DELETE FROM Livro"
                    banco.dml(comando_insanidade2)
                    tv.delete(*tv.get_children())
                    mb.showinfo("Operação realizada com sucesso!","Caso seja necessário, uma pasta de backup foi criada na mesma pasta desse prorama!")   
                else:
                    mb.showerror("Erro!","Não há livros cadastrados na biblioteca ainda!") 
            else:
                mb.showerror("Erro!","Há ao menos um livro ainda não devolvido. Por isso os registros da biblioteca não podem ser zerados!")   
                print(garantia)
        else:
            mb.showinfo("Operação cancelada!","A operação de 'Zerar banco' foi cancelada!")
    def janela_devolucao():
        if(Nome_pessoaDevolucao.get()!="" and cpf_pessoaDevolucao.get()!="" and id_livroDevolucao.get()!=""):
            if(regex_biblioteca.validanome(Nome_pessoaDevolucao.get()) and regex_biblioteca.validacpf(cpf_pessoaDevolucao.get())
               and regex_biblioteca.validaid(id_livroDevolucao.get())):
                nome=str(Nome_pessoaDevolucao.get())
                cpf=str(cpf_pessoaDevolucao.get())
                idLivro=str(id_livroDevolucao.get())
                comando="SELECT status FROM Livro WHERE id='"+idLivro+"';"
                if(banco.dql(comando)!=[('',)] or banco.dql(comando)!=[(None,)]):
                    excluirPessoa="DELETE FROM Pessoa WHERE cpf='"+cpf+"' and nome='"+nome+"';"
                    banco.dml(excluirPessoa)
                    mudarStatusLivro="UPDATE Livro SET status='',data_alug='',data_entrega='' WHERE id='"+idLivro+"';"
                    banco.dml(mudarStatusLivro)
                    mb.showinfo("Sucesso :)","Livro devolvido com sucesso!")
                else:
                    mb.showerror("Erro :(","Esse Livro não foi alugado!")
            else:
                mb.showwarning("ATENÇÃO","O campos devem ser preenchidos da seguinte forma:\n*Nome começando com Letra maiúscula*\n*CPF: 000.000.000-00*\n*Id até cinco caracteres, contendo letras ou números*")
        else:
            mb.showerror("Erro :(","Todos os campos devem ser preenchidos")
    def documentacao():
        janela_documentacao=tk.Tk()
        janela_documentacao.title("Biblioteca- Documentação")
        centralizar_janela(janela_documentacao,500,300)
        janela_documentacao.configure(background="#dde")
    def gerarConsultas():
        query_Livro="SELECT * FROM Livro,Pessoa WHERE status='Alugado';"
        resultado=banco.dql(query_Livro)
        if(resultado!=[]):
            for i in resultado:
                lista=(i)
                with open(""+pastaApp+"\\Consultas_Biblioteca.txt","w",encoding="UTF-8") as f:
                    f.write("%s(contato:%s) alugou %s(categoria:%s | id:%s) em %s \n\n"%(lista[9],lista[10],lista[0],lista[2],lista[6],lista[4]))
            mb.showinfo("Consulta feita :)","O arquivo com a lista dos livros alugados está na mesma pasta desse programa ")
        else:
            mb.showerror("ERRO :)","Não há nehum livro alugado até o momento!")
    def GerarBancoTxt():
        queryBancoLivros="SELECT * FROM Livro ORDER BY id"
        resultadoTodos=banco.dql(queryBancoLivros)
        if(resultadoTodos!=[]):
            for i in resultadoTodos:
                lista=(i)
                with open(""+pastaApp+"\\Livros_Cadastrados.txt","w",encoding="UTF-8") as f:
                    f.write("Livro:%s | Categoria:%s | Autor:%s | ID:%s"%(lista[0],lista[2],lista[3],lista[6]))
                    f.write("\n\n")
            mb.showinfo("Banco gerado com sucesso :)","O arquivo com a lista dos livros cadastrados está na mesma pasta desse programa ")      
    def Deleta_Livro():
        try:
            livroSelecionado=tv.selection()
            Lista_delete=[]
            for i in tv.item(livroSelecionado,'values'):
                Lista_delete.append(str(i))
            if mb.askyesno("ATENÇÃO", "Deseja realmente deletar o livro '"+Lista_delete[0]+"'?"):
                if(Lista_delete[1]!='Alugado'):
                    comando_deletar="DELETE FROM Livro WHERE id='"+Lista_delete[6]+"'"
                    banco.dml(comando_deletar)
                    if(banco.dml(comando_deletar)):
                        tv.delete(livroSelecionado)
                        mb.showinfo("Sucesso :)","Livro deletado com sucesso!")
                else:
                    mb.showerror("Erro!","O Livro'"+Lista_delete[0]+"' está alugado até '"+Lista_delete[5]+"' ")
        except:
            mb.showerror("Erro!","Selecione algum livro para que ele possa ser deletado da biblioteca.")
    def QuemAlugou():
        try:
            livroSelecionado=tv.selection()
            Lista_Consulta=[]
            for i in tv.item(livroSelecionado,'values'):
                Lista_Consulta.append(str(i))
            if Lista_Consulta[1]=='Alugado':
                
                janela_consulta=tk.Tk()
                janela_consulta.title("Biblioteca- Consultar empréstimo")
                centralizar_janela(janela_consulta,500,300)
                janela_consulta.configure(background="#dde")                           
                query_quem="SELECT * FROM Pessoa WHERE id_livro='"+Lista_Consulta[6]+"';"
                resultado_quem=banco.dql(query_quem)
                for i in resultado_quem:
                    lista_quem=(i)   
                texto=tk.LabelFrame(janela_consulta,text="Dados da Pessoa")
                texto.pack(fill="both",expand="yes",padx=10,pady=10,side="top")
                tk.Label(texto,text="Nome: "+lista_quem[2]+"",font="Arial 12 bold").pack()
                tk.Label(texto,text="Contato: "+lista_quem[3]+"",font="Arial 12 bold").pack()
                tk.Label(texto,text="CPF: "+lista_quem[0]+"",font="Arial 12 bold").pack()
                
                texto_nomeLivro=tk.LabelFrame(janela_consulta,text="Dados do Livro")
                texto_nomeLivro.pack(fill="y",expand="yes",padx=10,pady=10,side="left")
                tk.Label(texto_nomeLivro,text="Nome do Livro: "+Lista_Consulta[0]+"",font="Arial 12 bold").pack()
                texto_idLivro=tk.LabelFrame(janela_consulta,text="Dados do Livro")
                texto_idLivro.pack(fill="y",expand="yes",padx=10,pady=10,side="left")
                tk.Label(texto_idLivro,text="ID: "+Lista_Consulta[6]+"",font="Arial 12 bold").pack()
            else:
                mb.showerror("Erro!","O livro '"+Lista_Consulta[0]+"' não foi emprestado ainda")
        except:
            mb.showerror("Erro!","Selecione algum livro para que a consulta possa ser feita.")
        
    #cria a janela e define título
    janela = tk.Tk()
    janela.title("Biblioteca")
    #define largura e altura da janela
    largura=800
    altura=500
    #captura largura e altura da tela 
    largura_screen=janela.winfo_screenwidth()
    altura_screen=janela.winfo_screenheight()
    #calcula o meio
    posx=  (largura_screen/2)-(largura/2)
    posy= (altura_screen/2)-(altura/2)
    #posiciona a janela no meio e impede redimensionamento
    janela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))
    janela.resizable(False,False)
    janela.configure(background="#dde")
    #criar menu
    barraDeMenu=tk.Menu(janela)
    menuCRUD=tk.Menu(barraDeMenu, tearoff=0)
    menuCRUD.add_command(label="Gerar Banco",command=GerarBancoTxt)
    menuCRUD.add_command(label="Zerar Banco",command=zera_banco)
    menuCRUD.add_separator()
    menuCRUD.add_command(label="sair",command=verificacao_sair)
    barraDeMenu.add_cascade(label="Menu",menu=menuCRUD)
    janela.config(menu=barraDeMenu)
    #Criar segundo menu
    menuDOC=tk.Menu(barraDeMenu, tearoff=0)
    menuDOC.add_command(label="como funciona?",command=documentacao)
    barraDeMenu.add_cascade(label="Dúvidas",menu=menuDOC)
    janela.config(menu=barraDeMenu)
    #abas
    noteb=ttk.Notebook(janela)
    noteb.place(x=0,y=0,width=800,height=500)
    #aba de pesquisa
    pesquisar_aba=ttk.Frame(noteb)
    noteb.add(pesquisar_aba,text="Pesquisar Livro")
    #aba de cadastro
    cadastrar_aba=ttk.Frame(noteb)
    noteb.add(cadastrar_aba,text="Cadastrar Livro")
    #aba de empréstimo
    Emprestar_aba=ttk.Frame(noteb)
    noteb.add(Emprestar_aba,text="Empréstimo")
    #aba de devolução
    devolucao_aba=ttk.Frame(noteb)
    noteb.add(devolucao_aba,text="Devolução")
    #conteúdo aba de pesquisa
#caixa com a listagem dos livros
    quadroGrid=tk.LabelFrame(pesquisar_aba,text="Livros")
    quadroGrid.pack(fill="both",expand="yes",padx=10,pady=10)
    tv=ttk.Treeview(quadroGrid,columns=('nome','status','categoria','autor','empréstimo','entrega','id'),show='headings')
    tv.column('nome',minwidth=0,width=150)
    tv.column('status',minwidth=0,width=50)
    tv.column('categoria',minwidth=0,width=100)
    tv.column('autor',minwidth=0,width=100)
    tv.column('empréstimo',minwidth=0,width=100)
    tv.column('entrega',minwidth=0,width=100)
    tv.column('id',minwidth=0,width=50)
    tv.heading('nome',text="nome")
    tv.heading('status',text="status")
    tv.heading('categoria',text="categoria")
    tv.heading('autor',text="autor")
    tv.heading('empréstimo',text="empréstimo")
    tv.heading('entrega',text="entrega")
    tv.heading('id',text="id")
    tv.pack()
    popularGrid()
    tk.Button(quadroGrid,text="Consultar",pady=1,command=QuemAlugou,bg="#363636",fg="#fff",font="Arial 12 bold").pack(side="left",padx=5)
    tk.Button(quadroGrid,text="Gerar consultas",pady=1,command=gerarConsultas,bg="#363636",fg="#fff",font="Arial 12 bold").pack(side="left",padx=5)
    tk.Button(quadroGrid,text="Excluir Livro",pady=1,command=Deleta_Livro,bg="#363636",fg="#fff",font="Arial 12 bold").pack(side="left",padx=5)
    #campo de pesquisa
    quadroPesquisa=tk.LabelFrame(pesquisar_aba,text="Procurar")
    quadroPesquisa.pack(fill="both",expand="yes",padx=10,pady=10)
    pesquisar=tk.Entry(quadroPesquisa,width=50)
    pesquisar.pack(side="left",padx=10)
    #botão de pesquisa
    tk.Button(quadroPesquisa,text="Pesquisar",pady=1,command=procurar,bg="#363636",fg="#fff",font="Arial 12 bold").pack(side="left")
    tk.Button(quadroPesquisa,text="Mostrar todos",pady=1,command=popularGrid,bg="#363636",fg="#fff",font="Arial 12 bold").pack(side="left",padx="8")
    
    #conteúdo aba de cadastro
    quadroCadastro=tk.LabelFrame(cadastrar_aba,text="Nome do Livro")
    quadroCadastro.pack(fill="y",expand="no",padx=10,pady=10)
    #nome do livro
    Nome=tk.Entry(quadroCadastro,width=50)
    tk.Label(quadroCadastro,text="Nome do livro",font="Arial 12 bold").pack()
    Nome.pack()
    #categoria do livro
    valor=tk.StringVar()
    tk.Label(quadroCadastro,text="Selecione a categoria",font="Arial 12 bold").pack()
    categoria=ttk.Combobox(quadroCadastro,width=27,textvariable=valor)
    categorias_cadastradas="SELECT DISTINCT categoria FROM livro"
    resultado=banco.dql(categorias_cadastradas)
    categoria['values']=resultado
    categoria.pack()
    categoria.current()
    #autor do livro
    autor=tk.Entry(quadroCadastro,width=50)
    tk.Label(quadroCadastro,text="Autor(a) do livro",font="Arial 12 bold").pack()
    autor.pack()
    #botão de cadastro
    tk.Button(quadroCadastro,text="Cadastrar",pady=1,command=cont_abaCadastro,bg="#363636",fg="#fff",font="Arial 12 bold").pack(side="bottom",pady=8)
    #conteúdo aba de empréstimo
    #dados da pessoa
    #nome da pessoa
    quadroEmprestaPessoa=tk.LabelFrame(Emprestar_aba,text="Dados Pessoa")
    quadroEmprestaPessoa.pack(fill="none",expand="no",padx=10,pady=10)
    Nome_pessoa=tk.Entry(quadroEmprestaPessoa,width=50)
    tk.Label(quadroEmprestaPessoa,text="Nome:",font="Arial 12 bold").pack()
    Nome_pessoa.pack(padx=8,pady=8)
    #cpf da pessoa
    cpf_pessoa=tk.Entry(quadroEmprestaPessoa,width=50)
    tk.Label(quadroEmprestaPessoa,text="CPF:",font="Arial 12 bold").pack()
    cpf_pessoa.pack(padx=8,pady=8)
    #contato da pessoa
    contato_pessoa=tk.Entry(quadroEmprestaPessoa,width=50)
    tk.Label(quadroEmprestaPessoa,text="Telefone para Contato:",font="Arial 12 bold").pack()
    contato_pessoa.pack(padx=8,pady=8)
    #dados do livro emprestado
    quadroEmprestaLivro=tk.LabelFrame(Emprestar_aba,text="Dados Livro")
    quadroEmprestaLivro.pack(fill="none",expand="no",padx=10,pady=10)
    #nome do livro
    valor_ids=tk.StringVar()
    tk.Label(quadroEmprestaLivro,text="ID do livro",font="Arial 12 bold").pack()
    ID_livro=ttk.Combobox(quadroEmprestaLivro,width=15,textvariable=valor_ids)
    procura_ids="SELECT id FROM Livro"
    result_ids=banco.dql(procura_ids)
    ID_livro['values']=result_ids
    ID_livro.pack(padx=8,pady=8)
    ID_livro.current()
    #datas 
    data_emprestimo=tk.Entry(quadroEmprestaLivro,width=20)
    tk.Label(quadroEmprestaLivro,text="Data de empréstimo:",font="Arial 12 bold").pack()
    data_emprestimo.pack(padx=8,pady=8)
    data_entrega=tk.Entry(quadroEmprestaLivro,width=20)
    tk.Label(quadroEmprestaLivro,text="Data de entrega:",font="Arial 12 bold").pack()
    data_entrega.pack(padx=8,pady=8)
    #botao
    tk.Button(Emprestar_aba,text="Emprestar",command=cont_abaEmprestar,bg="#363636",fg="#fff",font="Arial 12 bold").pack(side="bottom")
    
    #aba de devolução
    #criação da janela de devolução
    quadroDevolveLivro=tk.LabelFrame(devolucao_aba,text="Devolução de Livro")
    quadroDevolveLivro.pack(fill="none",expand="no",padx=10,pady=10)
    Nome_pessoaDevolucao=tk.Entry(quadroDevolveLivro,width=50)
    tk.Label(quadroDevolveLivro,text="Nome:",font="Arial 12 bold").pack()
    Nome_pessoaDevolucao.pack(padx=8,pady=8)
        
    cpf_pessoaDevolucao=tk.Entry(quadroDevolveLivro,width=50)
    tk.Label(quadroDevolveLivro,text="CPF:",font="Arial 12 bold").pack()
    cpf_pessoaDevolucao.pack(padx=8,pady=8)

    valor_ids=tk.StringVar()
    tk.Label(quadroDevolveLivro,text="ID do livro",font="Arial 12 bold").pack()
    id_livroDevolucao=ttk.Combobox(quadroDevolveLivro,width=15,textvariable=valor_ids)
    procura_ids="SELECT id FROM Livro"
    result_ids=banco.dql(procura_ids)
    id_livroDevolucao['values']=result_ids
    id_livroDevolucao.pack(padx=8,pady=8)
    id_livroDevolucao.current()
    
    #botão que efetiva a devolução
    tk.Button(quadroDevolveLivro,text="Entregue",pady=1,command=janela_devolucao,bg="#363636",fg="#fff",font="Arial 12 bold").pack(pady=8)
except conector.DatabaseError as erro:
    print("Erro no Banco de Dados:", erro)
finally:
    tk.mainloop()
