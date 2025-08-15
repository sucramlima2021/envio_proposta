import pyodbc
from atualiza_nomes import atualiza
import datetime
import locale
import traceback
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
import sqlite3

tabelas = ['a_cifptd', 'a_educacional', 'a_mulher', 'a_sifptd', 'a136404', 'a136604', 'a136704', 'a136801', 'a137104', 'a2055', 'a2863', 'a2948', 'a3018', 'a3018ifptd', 'a3039', 'a3063', 'a3213', 'a3214', 'a3215', 'a3216', 'agregados', 'beneficiarios', 'clientes']
datamin = datetime.datetime(1923,1,1)


def dados_cliente(campo, valor, conn_str):
    
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    if campo == 'cpf': sql = f"select * from clientes where {campo} = '{valor}'"
    else: sql = f"select * from clientes where {campo} = {valor}"
    cursor.execute(sql)
    dados = cursor.fetchone()
    if dados:
        cliente_campos = {"matricula":str(dados[0]).split('.')[0],
              "nome":dados[1],
              "logradouro":dados[2],
              "numero":dados[3],
              "complemento":dados[4],
              "bairro":dados[5],
              "cidade":dados[6],
              "uf":dados[7],
              "telefone":dados[9],
              "celulares":dados[13],
              "rota":dados[14],
              "localizador":dados[15],
              "email":dados[19],
              "nascimento":dados[20],
              "cpf":dados[21],
              "rg":dados[22],
              "orgao":dados[23],
              "expedicao":dados[24],
              "estadocivil":dados[25],
              "cargo":dados[26],
              "funcao":dados[27],
              "angariador":dados[30],
              "conjuge":dados[42],
              "nascimentoconjuge":dados[43],
              "cpfconjuge":dados[44],
              "sexo":dados[51],
              "cep":dados[53],
              "controle":dados[57]    
              }
        conn.close()
        
        return cliente_campos
    else:
        conn.close()
        return False
  

def apolices_encontradas(controle, conn_str):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    apolicesEncontradas = []
    for i in tabelas:
        cursor.execute(f"select * from {i} where controle = '{controle}'")
        tt = cursor.fetchone()
       
        if tt:
            
            if i == 'clientes' or i == 'beneficiarios' or i == 'agregados':
                pass
            else:
                apolicesEncontradas.append({'tabela': i, 'dados': tt})
    if len(apolicesEncontradas)<1: return False
    return capitais(apolicesEncontradas, conn_str)


def capitais(apolices, conn_str):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    gg = []
    for i in apolices:
        valores = {}
        valores["apolice"] = atualiza(i['tabela'])
        camposPos = {
                        'premio' : '',
                        'premioconjuge' : '',
                        'is' : '',
                        'isConj' : '',
                        'movimento' : '',
                        'movimentoconjuge' : ''
                        }
        complNome = i['tabela'].replace('a', '')
        complNome = complNome.replace('_', '') 
        for r in cursor.columns(table=i['tabela']):
            if f'isbasicaconjuge{complNome}' == str(r.column_name).lower(): camposPos['isConj'] = r.ordinal_position - 1
            elif f'isbasica{complNome}' == str(r.column_name).lower(): camposPos['is'] = r.ordinal_position - 1
            elif f'movimentoconjuge{complNome}' == str(r.column_name).lower(): camposPos['movimentoconjuge'] = r.ordinal_position - 1
            elif f'movimento{complNome}' == str(r.column_name).lower(): camposPos['movimento'] = r.ordinal_position - 1
            elif f'premioconjuge{complNome}' == str(r.column_name).lower(): camposPos['premioconjuge'] = r.ordinal_position - 1
            elif f'premio{complNome}' == str(r.column_name).lower(): camposPos['premio'] = r.ordinal_position - 1
                    

        for key,val in camposPos.items():
            try:
                if type(i['dados'][val]) == float or type(i['dados'][val]) == int:
                    valores[key] = i['dados'][val]
                else: 
                    valores[key] = str(i['dados'][val])
            except:
                valores[key] = 0
        if valores['movimento'] != 'A':        
            gg.append(valores)
    
                
    if len(gg) < 1:
        return False
    div = {'vida1':[], 'vida2':[], 'mulher':[], 'funeral':[]}
    for i in gg:
        if i['apolice'] in ['1364-2', '1364-2A', '1364-1', '1364-3', '1364-4']: div['vida1'].append(i)
        elif i['apolice'] in ['1366-2', '1366-1', '1366-3', '1366-4']: div['vida2'].append(i)
        elif i['apolice'] in ['1371-1', '1371-2', '1371-3', '1371-4']: div['mulher'].append(i)
        elif i['apolice'] in ['1368-2']: div['funeral'].append(i)

    return div


def beneficiarios(controle, conn_str):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute(f"select * from beneficiarios where controle = '{controle}'")
    listBenef = {'vida':[], 'mulher':[]}
    benef = cursor.fetchall()
    if benef:
        for i in benef:
            if type(i[2]) == datetime.datetime:
                dd = i[2].strftime("%d/%m/%Y")
            else:
                dd = ''
            if i[0] == 'CIFPTD' or i[0] == 'SIFPTD' :
                listBenef['vida'].append({
                        'apolice':i[0],
                        'nome':i[1],
                        'nascimento':dd,
                        'cpf':i[3],
                        'parentesco':i[4],
                        'percentual':i[5],
                        'controle':i[6]
                    })
            elif i[0] == 'MULHER1':
                listBenef['mulher'].append({
                        'apolice':i[0],
                        'nome':i[1],
                        'nascimento':dd,
                        'cpf':i[3],
                        'parentesco':i[4],
                        'percentual':i[5],
                        'controle':i[6]
                    })
        return listBenef
    else:
        return False