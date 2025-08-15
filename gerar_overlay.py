# make_overlay.py
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from overlay_helpers import reg_font_kartika, draw_text, draw_checkbox, PAGE_W, PAGE_H
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import num2words

def gerar_overlay(val, fonte_ttf="kartika.ttf"):
    """
    Gera e retorna um BytesIO com o PDF 'overlay' (duas páginas A4) contendo apenas os textos e marcações.
    'dados' é um dict com os campos da sua proposta (nome, cpf, etc).
    """
    pdfmetrics.registerFont(TTFont('Kartika', 'kartika.ttf'))
    matricula = val['cpo_matricula']
    buff = BytesIO()
    c = canvas.Canvas(buff, pagesize=A4)
    c.setFont("Kartika", 12)  
    c.setTitle("Overlay da Proposta")

    # ============ PÁGINA 1 ============
    # Exemplos de campos (substitua as coordenadas mm pelos seus valores reais):
    # Cabeçalho (vigência, etc.)
   #Linha 1
    if val['cpo_vigenciade'] != '':
            inicio_txtl = val['cpo_vigenciade'].split('/')
            inicio_txt = f'{inicio_txtl[0]}  {inicio_txtl[1]}  {inicio_txtl[2]}'
    else: inicio_txt = ''  
    c.drawString(370, 770, inicio_txt)
    if val['cpo_vigenciaate'] != '':
            fim_txtl = val['cpo_vigenciaate'].split('/')
            fim_txt = f'{fim_txtl[0]}  {fim_txtl[1]}  {fim_txtl[2]}'
    else: fim_txt = ''  
    c.drawString(499, 770, fim_txt) 
        ###################

        #Linha 2
    estipulante = val['cpo_sub']
    c.drawString(19, 747, estipulante)
    codEstipulante = val['cpo_subcod']
    c.drawString(147, 747, codEstipulante) 
    codAngariador = val['cpo_angcod']
    c.drawString(286, 747, codAngariador)
    proposta = val['cpo_proposta']
    c.drawString(391, 747, proposta)
    sitAtivo_txt = ''
    if val['sit_ativo'] == 1: sitAtivo_txt = 'X'
    c.drawString(467,747,sitAtivo_txt)
    sitInativo_txt = ''
    if val['sit_inativo'] == 0: sitInativo_txt = 'X'
    c.drawString(521, 747, sitInativo_txt) 
        ###################

        #Linha 3
    sitProp = ''
    if val['sit_reint'] == 1: sitProp = 'X'
    c.drawString(19, 725, sitProp)
    checkVg1 = ''
    if val['vg1'] == 1: checkVg1 = 'X'
    c.drawString(146, 725, checkVg1)
    checkVg2 = ''
    if val['vg2'] == 1: checkVg2 = 'X'
    c.drawString(220, 725, checkVg2)
    checMulher = ''
    if val['vg3'] == 1: checMulher = 'X'
    c.drawString(294, 725, checMulher)
    checkFuneral = ''
    if val['af'] == 1: checkFuneral = 'X'
    c.drawString(378, 725, checkFuneral) 
        ###################

        #Linha 4
    proponente = val['cpo_prop']
    c.drawString(22, 679, proponente)

 ###################

        #Linha 5
    nasc = val['cpo_nasc']   
    c.drawString(22, 655, nasc)

    idade = val['cpo_idade']
    c.drawString(106, 655, idade)

    cpf = val['cpo_cpf']
    c.drawString(152, 655, cpf) 
       
    rg = val['cpo_rg']
    c.drawString(216, 655, rg)
    orgao = val['cpo_rgexp']
    c.drawString(300, 655, orgao)
    emissao = val['cpo_emiss']
    c.drawString(350, 655, emissao)
    sexoF = ''
    if val['fem'] == 1: sexoF = 'X'
       
    sexoM = ''
    if val['masc'] == 1: sexoM = 'X'
    c.drawString(400, 654, sexoM)
    c.drawString(420, 654, sexoF)
    estado = val['cpo_estcivil']
    c.drawString(270, 653, estado)
    
     ###################

        #Linha 5
    ocupacao = val['cpo_ocupacao']
    c.drawString(330, 653, ocupacao)
    matricula = val['cpo_matricula']
    c.drawString(495, 653, matricula) 
       
    localizador = val['cpo_localizador']
    c.drawString(22, 630, localizador)
    email = val['cpo_email']
    c.drawString(270, 630, email)
    rota = val['cpo_rota']
    c.drawString(474, 630, rota)
        ###################

        #Linha 6
    endereco = val['cpo_endereco']
    c.drawString(22, 606, endereco)
    numero = val['cpo_numero']
    c.drawString(378, 606, numero)
    complemento = val['cpo_compl']
    c.drawString(425, 606, complemento)
        ###################

        #Linha 7
    bairro = val['cpo_bairro']
    c.drawString(22, 582, bairro)
    cidade = val['cpo_cidade']
    c.drawString(215, 582, cidade)
    uf = val['cpo_uf']
    c.drawString(418, 582, uf)
    cep = val['cpo_cep']
    c.drawString(438, 582, cep)
    tel = val['cpo_tel']
    c.drawString(493, 582, tel)
        ###################

        #Linha 8
    emailP = val['cpo_emailp']
    c.drawString(22, 559, emailP)
    cel = val['cpo_celular']
    c.drawString(215, 559, cel)
    celW = val['cpo_whats']
    c.drawString(419, 559, celW)
        ###################
        
        #Linha 9
    conjuge = val['cpo_conjuge']
    c.drawString(22, 536, conjuge)
    nascC = val['cpo_nascimentoconj']
    c.drawString(324, 536, nascC)
    idadeC = val['cpo_idadeconj']
    c.drawString(425, 536, idadeC)
    cpfC = val['cpo_cpfconj']
    c.drawString(474, 536, cpfC)
        ###################

        #coberturas
        #Linha 1
    titular1 = val['lbltit1']
    c.drawString(63, 465, titular1)
    conjuge1 = val['lblconj1']
    c.drawString(100, 465, conjuge1)
    lmt1 = str(val['lblvct1'])
    c.drawString(360, 467, lmt1)
    lmc1 = str(val['lblvcc1'])
    c.drawString(442, 467, lmc1)
    total1 = str(val['lblvt1'])
    c.drawString(523, 466, total1)
        ###################

        #Linha 2
    titular2 = str(val['lbltit2'])
    c.drawString(63, 417, titular2)
    conjuge2 = str(val['lblconj2'])
    c.drawString(100, 417, conjuge2)
    lmt2 = str(val['lblvct2'])
    c.drawString(360, 417, lmt2)
    lmc2 = str(val['lblvcc2'])
    c.drawString(442, 417, lmc2)
    total2 = str(val['lblvt2'])
    c.drawString(523, 416, total2)
        ###################

        #Linha 3
    titular3 = str(val['lbltit3'])
    c.drawString(63, 372, titular3)
    conjuge3 = str(val['lblconj3'])
    c.drawString(100, 372, conjuge3)
    lmt3 = str(val['lblvct3'])
    c.drawString(360, 373, lmt3)
    total3 = str(val['lblvt3'])
    c.drawString(523, 373, total3)
        ###################

        #Linha 4
        #titular4 = str(val['lbltit4'])
        #c.drawString(63, 348, titular4)
        #conjuge4 = str(val['lblconj4'])
        #c.drawString(100, 348, conjuge4)
        #lmt4 = str(val['lblvct4'])
        #c.drawString(360, 348, lmt4)
        #total4 = str(val['lblvt4'])
        #c.drawString(523, 347, total4)
        ###################

        #Linha 6
    totalT = str(val['pmt'])
    c.drawString(523, 331, totalT)
        ###################

        #beneficiarios

        #Linha 1
    benev1 = str(val['lblbnome1'])
    c.drawString(22, 200, benev1)
    nascv1 = str(val['lblbnasc1'])
    c.drawString(280, 200, nascv1)
    parenv1 = str(val['lblbpare1'])
    c.drawString(390, 200, parenv1)
    partv1 = str(val['lblbpart1'])
    c.drawString(518, 200, partv1)
        ###################

        #Linha 2
    benev2 = str(val['lblbnome2'])
    c.drawString(22, 184, benev2)
    nascv2 = str(val['lblbnasc2'])
    c.drawString(280, 184, nascv2)
    parenv2 = str(val['lblbpare2'])
    c.drawString(390, 184, parenv2)
    partv2 = str(val['lblbpart2'])
    c.drawString(518, 184, partv2)
        ###################

        #Linha 3
    benev3 = str(val['lblbnome3'])
    c.drawString(22, 168, benev3)
    nascv3 = str(val['lblbnasc3'])
    c.drawString(280, 168, nascv3)
    parenv3 = str(val['lblbpare3'])
    c.drawString(390, 168, parenv3)
    partv3 = str(val['lblbpart3'])
    c.drawString(518, 168, partv3)
        ###################

        #Linha 4
    benev4 = str(val['lblbnome4'])
    c.drawString(22, 152, benev4)
    nascv4 = str(val['lblbnasc4'])
    c.drawString(280, 152, nascv4)
    parenv4 = str(val['lblbpare4'])
    c.drawString(390, 152, parenv4)
    partv4 = str(val['lblbpart4'])
    c.drawString(518, 152, partv4)
        ###################

        #Linha 5
    benem1 = str(val['lblbnome1M'])
    c.drawString(22, 103, benem1)
    nascm1 = str(val['lblbnasc1M'])
    c.drawString(280, 103, nascm1)
    parenm1 = str(val['lblbpare1M'])
    c.drawString(390, 103, parenm1)
    partm1 = str(val['lblbpart1M'])
    c.drawString(518, 103, partm1)
        ###################

        #Linha 6
    benem2 = str(val['lblbnome2M'])
    c.drawString(22, 87, benem2)
    nascm2 = str(val['lblbnasc2M'])
    c.drawString(280, 87, nascm2)
    parenm2 = str(val['lblbpare2M'])
    c.drawString(390, 87, parenm2)
    partm2 = str(val['lblbpart2M'])
    c.drawString(518, 87, partm2)
        ###################

        #Linha 6
    benem3 = str(val['lblbnome3M'])
    c.drawString(22, 71, benem3)
    nascm3 = str(val['lblbnasc3M'])
    c.drawString(280, 71, nascm3)
    parenm3 = str(val['lblbpare3M'])
    c.drawString(390, 71, parenm3)
    partm3 = str(val['lblbpart3M'])
    c.drawString(518, 71, partm3)
        ###################

        #Linha 7
    benem4 = str(val['lblbnome4M'])
    c.drawString(22, 55, benem4)
    nascm4 = str(val['lblbnasc4M'])
    c.drawString(280, 55, nascm4)
    parenm4 = str(val['lblbpare4M'])
    c.drawString(390, 55, parenm4)
    partm4 = str(val['lblbpart4M'])
    c.drawString(518, 55, partm4)
        ###################

    c.showPage()  # próxima página

    # ============ PÁGINA 2 ============
    # Exemplos: PPE, autorização de desconto, assinaturas etc.
    ppes = ''
    ppen = ''
    if val['ppe'] == 1: 
        ppes = 'X'
    else:
        ppen = 'X'
    c.drawString(24, 786, ppes)
    c.drawString(62, 786, ppen)


    pmtext = totalT.replace(',', '.')
    pmtext = "um dois três"#num2words(pmtext, lang='pt_BR', to='currency')
    c.drawString(118, 165, f'{totalT} ({pmtext.upper()})')

    titmat = val['titmat']
    mattit = val['mattit']

    c.drawString(35, 145, titmat)
    c.drawString(460, 145, mattit)
    
    c.showPage()
    c.save()
    buff.seek(0)
    return buff  # BytesIO com o overlay.pdf
