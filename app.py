import ttkbootstrap as tb
from ttkbootstrap import dialogs
from ttkbootstrap.constants import *
import sys
import sqlite3
from tkinter import filedialog as fd
from ttkbootstrap.tableview import Tableview
from utilidades import *
import datetime
import traceback
from buscar import *

from formulario import *

idUsuarioLogado = 0
tipoUsuarioLogado = 0
popup = False


def logar():
    global idUsuarioLogado, tipoUsuarioLogado
    usuario = username.get()
    senha = password.get()
    conn = sqlite3.connect('conf.db')
    cursor = conn.cursor()
    cursor.execute(f"select * from usuarios where nome = '{usuario}' and senha = '{senha}'")
    result = cursor.fetchone()
    conn.close()
    if result:    
        login.grid_forget()
        princ.grid()
        idUsuarioLogado = result[0]
        tipoUsuarioLogado = result[3]
        lblUsuLog.configure(text=result[1])
        exibe_parametros()
        if result[3] == 1:
            btn1.configure(state='disabled')
            
            btn3.configure(state='disabled')
            
        elif result[3] == 2:
            
            btn3.configure(state='enabled')
            btn1.configure(state='disabled')
            
        else:
            btn1.configure(state='enabled')
            
            btn3.configure(state='enabled')
            
        
    else:
        dialogs.Messagebox.show_warning('Usuário ou Senha inválidos.', 'Falha no Login')

def deslogar():
    princ.grid_forget()
    login.grid()
    username.delete(0,END)
    password.delete(0,END)

def selecionaBd():
    banco = fd.askopenfilename()
    if banco != '':
        conn = sqlite3.connect('conf.db')
        cursor = conn.cursor()
        cursor.execute('select caminho_bd from configuracoes where id = 1')
        if banco != cursor.fetchone()[0]:
            cursor.execute(f"update configuracoes set caminho_bd = '{banco}' where id = 1")
            
            conn.commit()
        conn.close()
        exibe_parametros()

def gravaValorFixo(campo, valor):
    global popup
    if valor != '':
        conn = sqlite3.connect('conf.db')
        cursor = conn.cursor()
        cursor.execute(f"update valores_fixos set {campo} = '{valor}' where id = 1")
        conn.commit()
        conn.close()
        exibe_parametros()
        popup.destroy()
    
def alteraDecesso():
    global popup
    popup = tb.Toplevel('Alterar Valor do Decesso')
    popup.grab_set()
    lbl = tb.Label(popup, text='Alterar valor do Decesso').grid(row = 0, column=0, columnspan=2, pady = 10, padx = 10)
    novoValor = tb.Entry(popup)
    novoValor.grid(row = 1, column= 0,columnspan = 2, pady = 20, padx = 20)
    btnGrava = tb.Button(popup, text='Gravar', command=lambda:gravaValorFixo('decesso', novoValor.get().replace(',', '.')))
    btnGrava.grid(row = 2, column= 0, padx = 10, pady = 10)
    btnFecha = tb.Button(popup, text='Fechar', command=lambda:popup.destroy())
    btnFecha.grid(row = 2, column= 1, padx = 10, pady = 10)

def pesq():
    
    cpo = campo.get()
    txt = controle.get()
    bd = caminhoBd.cget('text')
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        fr"DBQ={bd};"
        )
   
    cliente = dados_cliente(cpo, txt, conn_str)
    if cliente:
        if cliente['nascimentoconjuge'] and cliente['conjuge']:
            valido, tidade, cidade = valida_idade(cliente['nascimento'], cliente['nascimentoconjuge'])
        else:
            valido, tidade, cidade = valida_idade(cliente['nascimento'], False)
        if valido:
            valores = apolices_encontradas(cliente['controle'], conn_str)
            cliente['idade'] = tidade
            cliente['idadeconjuge'] = cidade
            if valores:
            
                vida1T = 0
                vida1C = 0
                vida1P = 0
                vida2T = 0
                vida2C = 0
                vida2P = 0
                mulherT = 0
                mulherP = 0
                #funeralT = float(decesso.cget('text'))
                funeralP = 0
                for k, v in valores.items():
                    for val in v:
                        if k == 'vida1':
                            if val['movimento'] != 'A':
                                vida1T += val['is']
                                if cidade != 0: 
                                    vida1C += val['isConj']
                                    vida1P += val['premioconjuge']
                                vida1P += val['premio'] 
                                
                        elif k == 'vida2':
                            if val['movimento'] != 'A':
                                vida2T += val['is']
                                if cidade != 0: 
                                    vida2C += val['isConj']
                                    vida2P += val['premioconjuge']
                                vida2P += val['premio'] 
                        elif k == 'mulher':
                            if val['movimento'] != 'A':
                                mulherT += val['is']
                                mulherP += val['premio']
                        elif k == 'funeral':
                            if val['movimento'] != 'A':
                                funeralP += val['premio']
                                vida1P += val['premio']
                totais = {'vida1T':vida1T, 
                          'vida1C':vida1C, 
                          'vida1P':vida1P, 
                          'vida2T':vida2T, 
                          'vida2C':vida2C, 
                          'vida2P':vida2P,
                          'mulherT':mulherT,
                          'mulherP':mulherP,
                          #'funeralT':funeralT,
                          'funeralP':funeralP,
                          'total':vida1P+vida2P+mulherP
                            } 
                #if totais['funeralP'] == 0: totais['funeralT'] = 0
                for k, v in totais.items():
                    if v == 0: totais[k] = ''
                    else: 
                        totais[k] = format(round(v, 2),'.2f').replace('.',',')

                
                benef = beneficiarios(cliente['controle'], conn_str)
                for k,v in cliente.items():
                    if type(v) == datetime.datetime and v.year < 1950: cliente[k] = ''
                    elif type(v) == datetime.datetime: cliente[k] = v.strftime("%d/%m/%Y")
                    elif type(v) == None or not v or v=='None': cliente[k] = ''
                val = [cliente, totais, benef]
                print(benef)
                chamaForm(val)
                
                #if pdf({'cliente':cliente, 'valores':valores, 'totais':totais, 'benef':benef}):
                #    visualizador()
                #else:
                #    print('Erro ao criar proposta')    

            else:
                dialogs.Messagebox.show_error('Nenhuma apólice para renovação foi encontrada.')   
        else:
            dialogs.Messagebox.show_error('Cliente ou cônjuge acima da idade limite.')
    else:
        dialogs.Messagebox.show_error('Cliente não encontrado.')
           

def exibe_parametros():
    conn = sqlite3.connect('conf.db')
    cursor = conn.cursor()
    cursor.execute("select caminho_bd from configuracoes where id = 1")
    result = cursor.fetchone()
    cursor.execute("select decesso from valores_fixos where id = 1")
    valFix = cursor.fetchone()
    conn.close()
    caminhoBd.configure(text=result[0], justify=CENTER)
    decesso.configure(text=valFix[0], justify=CENTER)

def crudUsuarios(op, **kwargs):
    global popup
    conn = sqlite3.connect('conf.db')
    cursor = conn.cursor()
    if op == 'criar':
        try:
            nome, senha, tipo = kwargs['nome'], kwargs['senha'], kwargs['tipo']
            sql = f"insert into usuarios(nome, senha, tipo) values('{nome}','{senha}', '{tipo}' )"
            cursor.execute(sql)
            dialogs.Messagebox.show_info('Usuário cadastrado com sucesso.')    
            conn.commit()
            conn.close()
        except Exception as e:
            dialogs.Messagebox.show_error('Erro ao executar esta ação.')
            with open('log.txt', 'w') as arq:
                arq.write(str(e))
                arq.write(traceback.format_exc())
        
    elif op == 'atualizar':
        try:
            id, nome, senha, tipo = kwargs['id'], kwargs['nome'], kwargs['senha'], kwargs['tipo']
            sql = f"update usuarios set nome = '{nome}', senha = '{senha}', tipo = '{tipo}' where id = '{id}'"
            cursor.execute(sql)
            dialogs.Messagebox.show_info('Dados alterados com sucesso.')    
            conn.commit()
            conn.close()
        except Exception as e:
            dialogs.Messagebox.show_error('Erro ao executar esta ação.')
            with open('log.txt', 'w') as arq:
                arq.write(str(e))
                arq.write(traceback.format_exc())

    elif op == 'atualizar2':
        try:
            id, nome, senha = kwargs['id'], kwargs['nome'], kwargs['senha']
            sql = f"update usuarios set nome = '{nome}', senha = '{senha}' where id = '{id}'"
            cursor.execute(sql)
            dialogs.Messagebox.show_info('Dados alterados com sucesso.')    
            
            conn.commit()
            conn.close()
        except Exception as e:
            dialogs.Messagebox.show_error('Erro ao executar esta ação.')
            with open('log.txt', 'w') as arq:
                arq.write(str(e))
                arq.write(traceback.format_exc())
            
    elif op == 'apagar':
        
        try:
            id = kwargs['id']
           
            if dialogs.Messagebox.okcancel(f'Tem certeza que quer excluir o usuário: {id}.') == 'OK':
                sql = f"delete from usuarios where id = '{id}'"
                cursor.execute(sql)
                dialogs.Messagebox.show_info('Usuário excluido com sucesso.')    
                
                conn.commit()
                conn.close()
                popup.destroy()
            else:
                popup.focus_set()
                popup.grab_set()
        except Exception as e:
            dialogs.Messagebox.show_error('Erro ao executar esta ação.')
            with open('log.txt', 'w') as arq:
                arq.write(str(e))
                arq.write(traceback.format_exc())

def usuarios():
    global popup
    if tipoUsuarioLogado != 3:
        conn = sqlite3.connect('conf.db')
        cursor = conn.cursor()
        cursor.execute(f"select nome, senha from usuarios where id = {idUsuarioLogado}")
        result = cursor.fetchone()
        conn.close()
        popup = tb.Toplevel('Gerenciar Usuário')
        popup.grab_set()
        lbltitulo = tb.Label(popup, text=f'Gerenciar Cadastro do Usuário: {result[0]}')
        lbltitulo.grid(padx = 10, pady = 10)
        frmForm = tb.Frame(popup)
        frmForm.grid(padx=10, pady = 10)
        lblNome = tb.Label(frmForm, text='Nome')
        lblNome.grid(row = 0, column=0, padx=5, pady=5)
        nome = tb.Entry(frmForm)
        nome.grid(row = 0, column= 1, padx=5, pady=5)
        nome.insert(0,result[0])
        lblSenha = tb.Label(frmForm, text='Senha')
        lblSenha.grid(row = 1, column=0, padx=5, pady=5)
        senha = tb.Entry(frmForm, show='*')
        senha.grid(row = 1, column= 1, padx=5, pady=5)
        senha.insert(0,result[1])
        frmBtn = tb.Frame(popup)
        frmBtn.grid(padx=10, pady = 10)
        grava = tb.Button(frmBtn, text='Gravar', command=lambda: crudUsuarios(op='atualizar2', id=idUsuarioLogado, nome=nome.get(), senha=senha.get())).grid(row=0, column=0, padx=5, pady=5)
        cancela = tb.Button(frmBtn, text='Cancelar', command=lambda: popup.destroy()).grid(row=0, column=1, padx=5, pady=5)
    else:    
        conn = sqlite3.connect('conf.db')
        cursor = conn.cursor()
        cursor.execute(f"select id, nome, tipo from usuarios")
        result = cursor.fetchall()
        conn.close()
        popup = tb.Toplevel('Gerenciar Usuários')
        popup.grab_set()
        popup.columnconfigure(0,weight=1)
        coldata = ['ID', 'Nome', 'Tipo']
        dt = Tableview(master=popup, coldata=coldata, rowdata=result, bootstyle=INFO, searchable=True)
        for i in dt.cidmap.keys():
                dt.align_column_center(cid=i)
                dt.align_heading_center(cid=i)
        dt.grid()
        dt.configure(selectmode='browse')

        frmComandos = tb.Frame(popup)
        frmComandos.grid(pady = 15)
        btnCad = tb.Button(frmComandos, text='Cadastrar', command=lambda:cmdAdmin(oper='criar')).grid(row = 0, column = 0, pady=5, padx=5)
        btnAlt = tb.Button(frmComandos, text='Alterar', command=lambda:cmdAdmin(oper='atualizar', id = dt.get_rows(selected=True)[0].values[0])).grid(row = 0, column = 1, pady=5, padx=5)
        btnDel = tb.Button(frmComandos, text='Apagar', command=lambda:crudUsuarios(op='apagar', id = dt.get_rows(selected=True)[0].values[0])).grid(row = 0, column = 2, pady=5, padx=5)
        btnFecha = tb.Button(frmComandos, text='Fechar', command=lambda:popup.destroy()).grid(row = 0, column = 3, pady=5, padx=5)

def cmdAdmin(oper, id = False):
        
        popup2 = tb.Toplevel('Gerenciar Usuário')
        popup2.grab_set()
        lbltitulo = tb.Label(popup2, text='Cadastrar Usuário')
        lbltitulo.grid(padx = 10, pady = 10)
        frmForm = tb.Frame(popup2)
        frmForm.grid(padx=10, pady = 10)
        lblNome = tb.Label(frmForm, text='Nome')
        lblNome.grid(row = 0, column=0, padx=5, pady=5)
        nome = tb.Entry(frmForm)
        nome.grid(row = 0, column= 1, padx=5, pady=5)
        lblSenha = tb.Label(frmForm, text='Senha')
        lblSenha.grid(row = 1, column=0, padx=5, pady=5)
        senha = tb.Entry(frmForm, show='*')
        senha.grid(row = 1, column= 1, padx=5, pady=5)
        lblTipo = tb.Label(frmForm, text='tipo')
        lblTipo.grid(row = 2, column=0, padx=5, pady=5)
        tipo = tb.Combobox(frmForm, values=(1,2,3))
        tipo.grid(row = 2, column= 1, padx=5, pady=5)
        tipo.set(1)
        frmBtn = tb.Frame(popup2)
        frmBtn.grid(padx=10, pady = 10)
        
        if oper == 'atualizar' and id:
            
            conn = sqlite3.connect('conf.db')
            cursor = conn.cursor()
            cursor.execute(f"select nome, senha, tipo from usuarios where id = '{id}'")
            result = cursor.fetchone()
            conn.close()
            nome.insert(0,result[0])
            senha.insert(0,result[1])
            tipo.set(result[2])
            lbltitulo.configure(text=f'Alterar cadastro do Usuário: {result[0]}')

        grava = tb.Button(frmBtn, text='Gravar', command=lambda: crudUsuarios(op=oper, id=id, nome=nome.get(), senha=senha.get(), tipo = tipo.get()))
        grava.grid(row=0, column=0, padx=5, pady=5)
        cancela = tb.Button(frmBtn, text='Cancelar', command=lambda: popup2.destroy())
        cancela.grid(row=0, column=1, padx=5, pady=5)

         


tela = tb.Window(title='Emissor de Propostas de Reintegração', themename="superhero", minsize=(750,750), maxsize=(750,750))
tela.columnconfigure(0, weight=1)
tela.rowconfigure(0, weight=1)
cores = tela.style.colors

#login
login = tb.Frame(tela)
login.grid()
lblLogin = tb.Label(login, text='Faça o Login para acessar.', font=("Helvetica", 16), justify='center')
lblLogin.grid(row=0, column=0,columnspan=2, padx=10, pady=10, sticky=EW)
sep = tb.Separator(login).grid(row=1,column=0, columnspan=2, sticky=EW, pady = (0,30))
lblusername = tb.Label(login, text='Username').grid(row=2, column=0, padx=10, pady=10)
username = tb.Entry(login)
username.grid(row = 2, column= 1, padx=10, pady=10)
lblusername = tb.Label(login, text='Senha').grid(row=3, column=0, padx=10, pady=10)
password = tb.Entry(login, show="*")
password.grid(row = 3, column= 1, padx=10, pady=10)
btnlogar = tb.Button(login, text='Login', command=logar).grid(row = 4, column= 0, columnspan=2, padx= 20, pady = 20, sticky=EW)


#main
princ = tb.Frame(tela)
princ.columnconfigure(0,weight=1)
princ.rowconfigure(0,weight=0)
princ.rowconfigure(1,weight=1)

menu = tb.Labelframe(princ, text='Configurações')
menu.grid(row = 0, column=0, padx=10, pady=10, sticky=EW)
btn1 = tb.Button(menu, text='Base de Dados', command=selecionaBd)
btn1.grid(row = 0, column=0, padx = 10, pady = 10)

btn3 = tb.Button(menu, text='Valor Decesso', command=alteraDecesso)
btn3.grid(row = 0, column=2, padx = 10, pady = 10)

btn4 = tb.Button(menu, text='Usuários', command=usuarios)
btn4.grid(row = 0, column=3, padx = 10, pady = 10)

params = tb.Labelframe(princ, text='Parâmetros')
params.grid(row = 1, column=0, padx=10, pady=10, sticky=EW)

lblbd = tb.Label(params, text='Base de dados:')
lblbd.grid(row=0, column=0, padx=5, pady=5, sticky=EW)
caminhoBd = tb.Label(params, text='c:/')
caminhoBd.grid(row=0, column=1, padx=5, pady=5, sticky=EW)

lblDecesso = tb.Label(params, text='IS DECESSO:')
lblDecesso.grid(row=2, column=0, padx=5, pady=5, sticky=EW)
decesso = tb.Label(params, text=' 4000')
decesso.grid(row=2, column=1, padx=5, pady=5, sticky=EW)

emitir = tb.Labelframe(princ, text='Preencher Proposta')
emitir.grid(row = 2, column=0, padx=10, pady=10, sticky=EW)
emitir.columnconfigure(1,weight=1)
lblCampo = tb.Label(emitir, text='Pesquisar por:').grid(row=0, column=0, padx=5, pady=5)
campo = tb.Combobox(emitir,values=('matricula', 'cpf'))
campo.set('matricula')
campo.grid(row=0, column=1, pady=5, padx=(5,25), sticky=EW)
lblControle = tb.Label(emitir, text='Número').grid(row=1, column=0, padx=5, pady=5)
controle = tb.Entry(emitir)
controle.grid(row=1, column=1, pady=5, padx=(5,25), sticky=EW)
pesquisa = tb.Button(emitir, text='Buscar dados', command=pesq)
pesquisa.grid(row=2, column=0, columnspan=2, padx=25, pady=20, sticky='ew')

usuLog = tb.Labelframe(princ, text='Usuário Logado:')
usuLog.grid(row = 3, column=0, padx=10, pady=10, sticky=EW)
usuLog.columnconfigure(1,weight=1)
lblUsuLog = tb.Label(usuLog, text=' ', justify='center')
lblUsuLog.grid(row=0, column=0, padx=5, pady=5, sticky=EW)
btnDeslogar = tb.Button(usuLog, text='Deslogar', command=deslogar).grid(row = 0, column=1, padx = 10, pady = 5, sticky=E)

fechar = tb.Button(princ, text='Fechar', command=lambda: sys.exit()).grid(row=4, column=0, padx=25, pady=20, sticky='ew')

if __name__ == '__main__': 
    tela.mainloop()