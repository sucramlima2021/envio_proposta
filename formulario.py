from tkinter import *

import ttkbootstrap as tb

from ttkbootstrap.constants import *
from ttkbootstrap import dialogs

from ttkbootstrap.scrolled import ScrolledFrame

from componentes import *

import datetime
from utilidades import *

datamin = datetime.datetime(1924,1,1)
campos = []
def chamaForm(valores):
    telatop = tb.Toplevel('formulário')
    telatop.columnconfigure(0, weight=1)
    telatop.rowconfigure(0, weight=1)
    sf = ScrolledFrame(telatop, height=500, width=1150)
    sf.grid(sticky=NSEW, padx=10, pady=10)
    stage = tb.Frame(sf)
    stage.grid()
    stage.columnconfigure(0, weight=1)
    stage.rowconfigure(0, weight=1)

    parte1 = tb.Frame(stage)
    parte1.grid(padx=10, sticky=EW)
       

    parte2 = tb.Frame(stage)
    parte2.grid(padx=10, sticky=EW)
    

    parte3 = tb.Frame(stage)
    parte3.grid(padx=10, sticky=EW)
    

    parte4 = tb.Frame(stage)
    parte4.grid(padx=10, sticky=EW)
    
    linha1 = tb.Frame(parte1)
    linha1.grid(sticky=EW)
    linha1.columnconfigure(0, weight=1)
    
    linha2 = tb.Frame(parte1)
    linha2.grid(sticky=EW)
    linha2.columnconfigure(0, weight=1)

    linha3 = tb.Frame(parte1)
    linha3.grid(sticky=EW)

    frm_estipulante = Bframe(linha1)
    frm_estipulante.grid(row=0, column=0, padx=2, pady=2, sticky=NSEW)
    lbl_estipulante = tb.Label(frm_estipulante.dentro, text="Estipulante")
    lbl_estipulante.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    cpo_estipulante = tb.Label(frm_estipulante.dentro, text="FCEPE – FEDERAÇÃO DOS CLUBES DOS EMPREGADOS DA PETROBRAS")
    cpo_estipulante.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)

    frm_cnpj = Bframe(linha1)
    frm_cnpj.grid(row=0, column=1, padx=2, pady=2, sticky=NSEW)
    lbl_cnpj = tb.Label(frm_cnpj.dentro, text="CNPJ")
    lbl_cnpj.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    cpo_cnpj = tb.Label(frm_cnpj.dentro, text="01.497.896/0001-29")
    cpo_cnpj.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)

   
    cpo_vigenciade = Lcampo(linha1, texto="Vigencia de:", data=True)
    cpo_vigenciade.grid(row=0, column=2, padx=2, pady=2)
    
    
    cpo_vigenciaate = Lcampo(linha1, texto="Vigencia até:", data = True)
    cpo_vigenciaate.grid(row=0, column=3, padx=2, pady=2)
    
    
    cpo_sub = Lcampo(linha2, texto="Sub-estipulante")
    cpo_sub.grid(row=0, column=0, padx=2, pady=2, sticky=NSEW)

    cpo_subcod = Lcampo(linha2, texto="Cod Sub-estipulante")
    cpo_subcod.grid(row=0, column=1, padx=2, pady=2, sticky=NSEW)

    cpo_angcod = Lcampo(linha2, texto="Cod. Angariador")
    cpo_angcod.grid(row=0, column=2, padx=2, pady=2, sticky=EW)

    cpo_proposta = Lcampo(linha2, texto="Proposta")
    cpo_proposta.grid(row=0, column=3, padx=2, pady=2, sticky=EW)

    frm_situacao = Bframe(linha2)
    frm_situacao.grid(row=0, column=4, sticky=NSEW, padx=2, pady=2)
    lbl_situacao = tb.Label(frm_situacao.dentro, text="situação do proponente")
    lbl_situacao.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=NSEW)
    sit_ativo = Lcheck(frm_situacao.dentro, texto="Ativo")
    sit_ativo.grid(row=1, column=0, sticky=NS, pady=5)
    sit_inativo = Lcheck(frm_situacao.dentro, texto="Inativo")
    sit_inativo.grid(row=1, column=1, sticky=NS, pady=5)

    frm_situacao2 = Bframe(linha3)
    frm_situacao2.grid(row=0, column=0, sticky=NSEW, padx=2, pady=2)
    lbl_situacao2 = tb.Label(frm_situacao2.dentro, text="situação do proponente")
    lbl_situacao2.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky=EW)
    sit_reint = Lcheck(frm_situacao2.dentro, texto="Reintegração")
    sit_reint.grid(row=1, column=0, sticky=NS, pady=5)

    frm_apoativ = Bframe(linha3)
    frm_apoativ.grid(row=0, column=1, sticky=NSEW, padx=2, pady=2)
    lbl_apoativ = tb.Label(frm_apoativ.dentro, text="Apólices ativas para reintegração")
    lbl_apoativ.grid(row=0, column=0, padx=5, pady=5, columnspan=4, sticky=EW)
    vg1 = Lcheck(frm_apoativ.dentro, texto="VG.1(Vida)")
    vg1.grid(row=1, column=0, sticky=NS, pady=5)
    vg2 = Lcheck(frm_apoativ.dentro, texto="VG.2(Vida)")
    vg2.grid(row=1, column=1, sticky=NS, pady=5, padx=5)
    vg3 = Lcheck(frm_apoativ.dentro, texto="VG.3(Mulher)")
    vg3.grid(row=1, column=2, sticky=NS, pady=5, padx=5)
    af = Lcheck(frm_apoativ.dentro, texto="Assistência Funeral")
    af.grid(row=1, column=3, sticky=NS, pady=5)

    p2l1 = tb.Frame(parte2)
    p2l1.grid(sticky=EW, pady = (20,5))
    infoprop = tb.Label(p2l1, text="Informações do Proponente", anchor="center")
    infoprop.grid(row=0, column=0, sticky=NSEW)
   
    p2l2 = tb.Frame(parte2)
    p2l2.grid(sticky=EW)
    p2l2.columnconfigure(0, weight=1)

    cpo_prop = Lcampo(p2l2, texto="Proponente principal")
    cpo_prop.grid(row=0, column=0, padx=2, pady=2, sticky=NSEW)
    
    cpo_nasc = Lcampo(p2l2, texto="Data de nascimento", data=True)
    cpo_nasc.grid(row=0, column=1, padx=2, pady=2, sticky=NSEW)

    cpo_idade = Lcampo(p2l2, texto="Idade", width=5)
    cpo_idade.grid(row=0, column=2, padx=2, pady=2, sticky=NSEW)

    cpo_cpf = Lcampo(p2l2, texto="CPF")
    cpo_cpf.grid(row=0, column=3, padx=2, pady=2, sticky=NSEW)
    
    p2l3 = tb.Frame(parte2)
    p2l3.grid(sticky=EW)
    p2l3.columnconfigure(0, weight=1)

    cpo_rg = Lcampo(p2l3, texto="Identidade")
    cpo_rg.grid(row=0, column=0, padx=2, pady=2, sticky=NSEW)
    
    cpo_rgexp = Lcampo(p2l3, texto="Órgão Exp.")
    cpo_rgexp.grid(row=0, column=1, padx=2, pady=2, sticky=NSEW)
    
    cpo_emiss = Lcampo(p2l3, texto="Emissão", width=10, data=True)
    cpo_emiss.grid(row=0, column=2, padx=2, pady=2, sticky=NSEW)
    
    frm_sexo = Bframe(p2l3)
    frm_sexo.grid(row=0, column=3, sticky=NSEW, padx=2, pady=2)
    lbl_sexo = tb.Label(frm_sexo.dentro, text="Sexo")
    lbl_sexo.grid(row=0, column=0, padx=5, pady=5, columnspan=4, sticky=EW)
    masc = Lcheck(frm_sexo.dentro, texto="M")
    masc.grid(row=1, column=0, sticky=NS, pady=5)
    fem = Lcheck(frm_sexo.dentro, texto="F")
    fem.grid(row=1, column=1, sticky=NS, pady=5, padx=5)
    
    cpo_estcivil = Lcampo(p2l3, texto="Estado Civil")
    cpo_estcivil.grid(row=0, column=4, padx=2, pady=2, sticky=NSEW)

    cpo_ocupacao = Lcampo(p2l3, texto="Ocupação")
    cpo_ocupacao.grid(row=0, column=5, padx=2, pady=2, sticky=NSEW)

    cpo_matricula = Lcampo(p2l3, texto="Matricula/CB", width=10)
    cpo_matricula.grid(row=0, column=6, padx=2, pady=2, sticky=NSEW)

    p2l4 = tb.Frame(parte2)
    p2l4.grid(sticky=EW)
    p2l4.columnconfigure(0, weight=1)

    cpo_localizador = Lcampo(p2l4, texto="Localizador")
    cpo_localizador.grid(row=0, column=0, padx=2, pady=2, sticky=NSEW)

    cpo_email = Lcampo(p2l4, texto="e-mail", width=70)
    cpo_email.grid(row=0, column=1, padx=2, pady=2, sticky=NSEW)

    cpo_rota = Lcampo(p2l4, texto="Rota", width=30)
    cpo_rota.grid(row=0, column=2, padx=2, pady=2, sticky=NSEW)

    p2l5 = tb.Frame(parte2)
    p2l5.grid(sticky=EW)
    p2l5.columnconfigure(0, weight=1)

    cpo_endereco = Lcampo(p2l5, texto="Endereço Residencial do Proponente Principal")
    cpo_endereco.grid(row=0, column=0, padx=2, pady=2, sticky=NSEW)

    cpo_numero = Lcampo(p2l5, texto="Número", width=5)
    cpo_numero.grid(row=0, column=1, padx=2, pady=2, sticky=NSEW)

    cpo_compl = Lcampo(p2l5, texto="Complemento", width=40)
    cpo_compl.grid(row=0, column=2, padx=2, pady=2, sticky=NSEW)

    p2l6 = tb.Frame(parte2)
    p2l6.grid(sticky=EW)
    p2l6.columnconfigure(0, weight=1)

    cpo_bairro = Lcampo(p2l6, texto="Bairro")
    cpo_bairro.grid(row=0, column=0, padx=2, pady=2, sticky=NSEW)

    cpo_cidade = Lcampo(p2l6, texto="Cidade", width=40)
    cpo_cidade.grid(row=0, column=1, padx=2, pady=2, sticky=NSEW)

    cpo_uf = Lcampo(p2l6, texto="UF", width=5)
    cpo_uf.grid(row=0, column=2, padx=2, pady=2, sticky=NSEW)

    cpo_cep = Lcampo(p2l6, texto="CEP", width=10)
    cpo_cep.grid(row=0, column=3, padx=2, pady=2, sticky=NSEW)

    cpo_tel = Lcampo(p2l6, texto="Telefone", width=15)
    cpo_tel.grid(row=0, column=4, padx=2, pady=2, sticky=NSEW)

    p2l7 = tb.Frame(parte2)
    p2l7.grid(sticky=EW)
    p2l7.columnconfigure(0, weight=1)

    cpo_emailp = Lcampo(p2l7, texto="Email Pessoal", width=50)
    cpo_emailp.grid(row=0, column=0, padx=2, pady=2, sticky=NSEW)

    cpo_celular = Lcampo(p2l7, texto="Celular", width=25)
    cpo_celular.grid(row=0, column=1, padx=2, pady=2, sticky=NSEW)

    cpo_whats = Lcampo(p2l7, texto="WhatsApp", width=25)
    cpo_whats.grid(row=0, column=2, padx=2, pady=2, sticky=NSEW)

    p2l8 = tb.Frame(parte2)
    p2l8.grid(sticky=EW)
    p2l8.columnconfigure(0, weight=1)

    cpo_conjuge = Lcampo(p2l8, texto="Conjuge", width=50)
    cpo_conjuge.grid(row=0, column=0, padx=2, pady=2, sticky=NSEW)

    cpo_nascimentoconj = Lcampo(p2l8, texto="Nascimento", data=True)
    cpo_nascimentoconj.grid(row=0, column=1, padx=2, pady=2, sticky=NSEW)

    cpo_idadeconj = Lcampo(p2l8, texto="Idade", width=5)
    cpo_idadeconj.grid(row=0, column=2, padx=2, pady=2, sticky=NSEW)

    cpo_cpfconj = Lcampo(p2l8, texto="Cpf")
    cpo_cpfconj.grid(row=0, column=3, padx=2, pady=2, sticky=NSEW)

    p3l1 = tb.Frame(parte3)
    p3l1.grid(sticky=EW, pady = (20,5))
   
    lbl1 = Bframe(p3l1)
    lbl1.grid(row=0, column=0, sticky=NSEW)
    lblprod = tb.Label(lbl1.dentro, text="Produto\nApólice ", anchor="center")
    lblprod.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)
    
    
    lbl2 = Bframe(p3l1)
    lbl2.grid(row=0, column=1, columnspan=2, sticky=NSEW)
    lblplano = tb.Label(lbl2.dentro, text="Plano\nTitular / Conjuge", anchor="center")
    lblplano.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    lbl3 = Bframe(p3l1)
    lbl3.grid(row=0, column=3, sticky=NSEW)
    
    lblcob = tb.Label(lbl3.dentro, text="Coberturas Contratadas\n", anchor="center")
    lblcob.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    lbl4 = Bframe(p3l1)
    lbl4.grid(row=0, column=4, sticky=NSEW)
    lbllct = tb.Label(lbl4.dentro, text="Limite máximo do \ncapital segurado titular", anchor="center")
    lbllct.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    lbl5 = Bframe(p3l1)
    lbl5.grid(row=0, column=5, sticky=NSEW)
    lbllcc = tb.Label(lbl5.dentro, text="Limite máximo do \ncapital segurado conjuge", anchor="center")
    lbllcc.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    
    lbl6 = Bframe(p3l1)
    lbl6.grid(row=0, column=6, sticky=NSEW)
    lblpretot = tb.Label(lbl6.dentro, text="Premio Total\n", anchor="center")
    lblpretot.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    
    
    lbl21 = Bframe(p3l1)
    lbl21.grid(row=1, column=0, sticky=NSEW)
    lblvida1 = tb.Label(lbl21.dentro, text="VIDA.1 ", anchor="center")
    lblvida1.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl22 = Bframe(p3l1)
    lbl22.grid(row=1, column=1, sticky=NSEW)
    lbltit1 = tb.Entry(lbl22.dentro, width=7)
    lbltit1.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl23 = Bframe(p3l1)
    lbl23.grid(row=1, column=2, sticky=NSEW)
    lblconj1 = tb.Entry(lbl23.dentro, width=7)
    lblconj1.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl24 = Bframe(p3l1)
    lbl24.grid(row=1, column=3, sticky=NSEW)
    lblcob1 = tb.Entry(lbl24.dentro)
    lblcob1.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblcob1.configure(state="readonly")
    lbl25 = Bframe(p3l1)
    lbl25.grid(row=1, column=4, sticky=NSEW)
    lblvct1 = tb.Entry(lbl25.dentro)
    lblvct1.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl26 = Bframe(p3l1)
    lbl26.grid(row=1, column=5, sticky=NSEW)
    lblvcc1 = tb.Entry(lbl26.dentro)
    lblvcc1.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl27 = Bframe(p3l1)
    lbl27.grid(row=1, column=6, sticky=NSEW)
    lblvt1 = tb.Entry(lbl27.dentro)
    lblvt1.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    lbl31 = Bframe(p3l1)
    lbl31.grid(row=2, column=0, sticky=NSEW)
    lblvida2 = tb.Label(lbl31.dentro, text="VIDA.2 ", anchor="center")
    lblvida2.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl32 = Bframe(p3l1)
    lbl32.grid(row=2, column=1, sticky=NSEW)
    lbltit2 = tb.Entry(lbl32.dentro, width=7)
    lbltit2.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl33 = Bframe(p3l1)
    lbl33.grid(row=2, column=2, sticky=NSEW)
    lblconj2 = tb.Entry(lbl33.dentro, width=7)
    lblconj2.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl34 = Bframe(p3l1)
    lbl34.grid(row=2, column=3, sticky=NSEW)
    lblcob2 = tb.Entry(lbl34.dentro)
    lblcob2.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblcob2.configure(state="readonly")
    lbl35 = Bframe(p3l1)
    lbl35.grid(row=2, column=4, sticky=NSEW)
    lblvct2 = tb.Entry(lbl35.dentro)
    lblvct2.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl36 = Bframe(p3l1)
    lbl36.grid(row=2, column=5, sticky=NSEW)
    lblvcc2 = tb.Entry(lbl36.dentro)
    lblvcc2.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl37 = Bframe(p3l1)
    lbl37.grid(row=2, column=6, sticky=NSEW)
    lblvt2 = tb.Entry(lbl37.dentro)
    lblvt2.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    lbl41 = Bframe(p3l1)
    lbl41.grid(row=3, column=0, sticky=NSEW)
    lblvida3 = tb.Label(lbl41.dentro, text="Mulher ", anchor="center")
    lblvida3.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl42 = Bframe(p3l1)
    lbl42.grid(row=3, column=1, sticky=NSEW)
    lbltit3 = tb.Entry(lbl42.dentro, width=7)
    lbltit3.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl43 = Bframe(p3l1)
    lbl43.grid(row=3, column=2, sticky=NSEW)
    lblconj3 = tb.Entry(lbl43.dentro, width=7)
    lblconj3.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl44 = Bframe(p3l1)
    lbl44.grid(row=3, column=3, sticky=NSEW)
    lblcob3 = tb.Entry(lbl44.dentro)
    lblcob3.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblcob3.configure(state="readonly")
    lbl45 = Bframe(p3l1)
    lbl45.grid(row=3, column=4, sticky=NSEW)
    lblvct3 = tb.Entry(lbl45.dentro)
    lblvct3.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl46 = Bframe(p3l1)
    lbl46.grid(row=3, column=5, sticky=NSEW)
    lblvcc3 = tb.Entry(lbl46.dentro)
    lblvcc3.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblvcc3.configure(state="readonly")
    lbl47 = Bframe(p3l1)
    lbl47.grid(row=3, column=6, sticky=NSEW)
    lblvt3 = tb.Entry(lbl47.dentro)
    lblvt3.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    '''lbl51 = Bframe(p3l1)
    lbl51.grid(row=4, column=0, sticky=NSEW)
    lblvida4 = tb.Label(lbl51.dentro, text="Funeral ", anchor="center")
    lblvida4.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl52 = Bframe(p3l1)
    lbl52.grid(row=4, column=1, sticky=NSEW)
    lbltit4 = tb.Entry(lbl52.dentro, width=7)
    lbltit4.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl53 = Bframe(p3l1)
    lbl53.grid(row=4, column=2, sticky=NSEW)
    lblconj4 = tb.Entry(lbl53.dentro, width=7)
    lblconj4.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl54 = Bframe(p3l1)
    lbl54.grid(row=4, column=3, sticky=NSEW)
    lblcob4 = tb.Entry(lbl54.dentro)
    lblcob4.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl55 = Bframe(p3l1)
    lbl55.grid(row=4, column=4, sticky=NSEW)
    lblvct4 = tb.Entry(lbl55.dentro)
    lblvct4.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl56 = Bframe(p3l1)
    lbl56.grid(row=4, column=5, sticky=NSEW)
    lblvcc4 = tb.Entry(lbl56.dentro)
    lblvcc4.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblvcc4.configure(state="readonly")
    lbl57 = Bframe(p3l1)
    lbl57.grid(row=4, column=6, sticky=NSEW)
    lblvt4 = tb.Entry(lbl57.dentro)
    lblvt4.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)'''

    
    
    lbl66 = Bframe(p3l1)
    lbl66.grid(row=5, column=5, sticky=NSEW)
    lblpmt = tb.Label(lbl66.dentro, text='Prêmio Mensal Total', anchor='center')
    lblpmt.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lbl67 = Bframe(p3l1)
    lbl67.grid(row=5, column=6, sticky=NSEW)
    pmt = tb.Entry(lbl67.dentro)
    pmt.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)





    p4l0 = tb.Frame(parte4)
    p4l0.grid(sticky=EW, pady = (20,5))
    infobene = tb.Label(p4l0, text="Informações dos beneficiários Vida 1 e 2", anchor="center")
    infobene.grid(row=0, column=0, sticky=NSEW)

    p4l1 = tb.Frame(parte4)
    p4l1.grid(sticky=EW, pady = (5,5))
    p4l1.columnconfigure(0, weight=1)
    nc = Bframe(p4l1)
    nc.grid(row=0, column=0, sticky=NSEW)
    lblbnome = tb.Label(nc.dentro, text="Nome Completo ", anchor="center")
    lblbnome.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)
    
    nsc = Bframe(p4l1)
    nsc.grid(row=0, column=1, sticky=NSEW)
    lblbnasc = tb.Label(nsc.dentro, text="Nascimento", anchor="center")
    lblbnasc.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    pare = Bframe(p4l1)
    pare.grid(row=0, column=2, sticky=NSEW)
    lblbpare = tb.Label(pare.dentro, text="Parentesco", anchor="center")
    lblbpare.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    part = Bframe(p4l1)
    part.grid(row=0, column=3, sticky=NSEW)
    lblbpart = tb.Label(part.dentro, text="Participação", anchor="center")
    lblbpart.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    nc1 = Bframe(p4l1)
    nc1.grid(row=1, column=0, sticky=NSEW)
    lblbnome1 = tb.Entry(nc1.dentro, width=50)
    lblbnome1.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)
    
    nsc1 = Bframe(p4l1)
    nsc1.grid(row=1, column=1, sticky=NSEW)
    lblbnasc1 = tb.DateEntry(nsc1.dentro)
    lblbnasc1.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblbnasc1.entry.delete(0,END)

    pare1 = Bframe(p4l1)
    pare1.grid(row=1, column=2, sticky=NSEW)
    lblbpare1 = tb.Entry(pare1.dentro)
    lblbpare1.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    part1 = Bframe(p4l1)
    part1.grid(row=1, column=3, sticky=NSEW)
    lblbpart1 = tb.Entry(part1.dentro)
    lblbpart1.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)


    nc2 = Bframe(p4l1)
    nc2.grid(row=2, column=0, sticky=NSEW)
    lblbnome2 = tb.Entry(nc2.dentro, width=50)
    lblbnome2.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)
    
    nsc2 = Bframe(p4l1)
    nsc2.grid(row=2, column=1, sticky=NSEW)
    lblbnasc2 = tb.DateEntry(nsc2.dentro)
    lblbnasc2.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblbnasc2.entry.delete(0,END)

    pare2 = Bframe(p4l1)
    pare2.grid(row=2, column=2, sticky=NSEW)
    lblbpare2 = tb.Entry(pare2.dentro)
    lblbpare2.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    part2 = Bframe(p4l1)
    part2.grid(row=2, column=3, sticky=NSEW)
    lblbpart2 = tb.Entry(part2.dentro)
    lblbpart2.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)


    nc3 = Bframe(p4l1)
    nc3.grid(row=3, column=0, sticky=NSEW)
    lblbnome3 = tb.Entry(nc3.dentro, width=50)
    lblbnome3.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)
    
    nsc3 = Bframe(p4l1)
    nsc3.grid(row=3, column=1, sticky=NSEW)
    lblbnasc3 = tb.DateEntry(nsc3.dentro)
    lblbnasc3.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblbnasc3.entry.delete(0,END)

    pare3 = Bframe(p4l1)
    pare3.grid(row=3, column=2, sticky=NSEW)
    lblbpare3 = tb.Entry(pare3.dentro)
    lblbpare3.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    part3 = Bframe(p4l1)
    part3.grid(row=3, column=3, sticky=NSEW)
    lblbpart3 = tb.Entry(part3.dentro)
    lblbpart3.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    nc4 = Bframe(p4l1)
    nc4.grid(row=4, column=0, sticky=NSEW)
    lblbnome4 = tb.Entry(nc4.dentro, width=50)
    lblbnome4.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)
    
    nsc4 = Bframe(p4l1)
    nsc4.grid(row=4, column=1, sticky=NSEW)
    lblbnasc4 = tb.DateEntry(nsc4.dentro)
    lblbnasc4.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblbnasc4.entry.delete(0,END)

    pare4 = Bframe(p4l1)
    pare4.grid(row=4, column=2, sticky=NSEW)
    lblbpare4 = tb.Entry(pare4.dentro)
    lblbpare4.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    part4 = Bframe(p4l1)
    part4.grid(row=4, column=3, sticky=NSEW)
    lblbpart4 = tb.Entry(part4.dentro)
    lblbpart4.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)




    p4l2 = tb.Frame(parte4)
    p4l2.grid(sticky=EW, pady = (20,5))
    infobenem = tb.Label(p4l2, text="Informações dos beneficiários Vida 3 Mulher", anchor="center")
    infobenem.grid(row=0, column=0, sticky=NSEW)

    p4l3 = tb.Frame(parte4)
    p4l3.grid(sticky=EW, pady = (5,5))
    p4l3.columnconfigure(0, weight=1)
    ncM = Bframe(p4l3)
    ncM.grid(row=0, column=0, sticky=NSEW)
    lblbnomeM = tb.Label(ncM.dentro, text="Nome Completo ", anchor="center")
    lblbnomeM.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)
    
    nscM = Bframe(p4l3)
    nscM.grid(row=0, column=1, sticky=NSEW)
    lblbnascM = tb.Label(nscM.dentro, text="Nascimento", anchor="center")
    lblbnascM.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    pareM = Bframe(p4l3)
    pareM.grid(row=0, column=2, sticky=NSEW)
    lblbpareM = tb.Label(pareM.dentro, text="Parentesco", anchor="center")
    lblbpareM.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    partM = Bframe(p4l3)
    partM.grid(row=0, column=3, sticky=NSEW)
    lblbpartM = tb.Label(partM.dentro, text="Participação", anchor="center")
    lblbpartM.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    nc1M = Bframe(p4l3)
    nc1M.grid(row=1, column=0, sticky=NSEW)
    lblbnome1M = tb.Entry(nc1M.dentro, width=50)
    lblbnome1M.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)
    
    nsc1M = Bframe(p4l3)
    nsc1M.grid(row=1, column=1, sticky=NSEW)
    lblbnasc1M = tb.DateEntry(nsc1M.dentro)
    lblbnasc1M.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblbnasc1M.entry.delete(0,END)

    pare1M = Bframe(p4l3)
    pare1M.grid(row=1, column=2, sticky=NSEW)
    lblbpare1M = tb.Entry(pare1M.dentro)
    lblbpare1M.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    part1M = Bframe(p4l3)
    part1M.grid(row=1, column=3, sticky=NSEW)
    lblbpart1M = tb.Entry(part1M.dentro)
    lblbpart1M.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)


    nc2M = Bframe(p4l3)
    nc2M.grid(row=2, column=0, sticky=NSEW)
    lblbnome2M = tb.Entry(nc2M.dentro, width=50)
    lblbnome2M.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)
    
    nsc2M = Bframe(p4l3)
    nsc2M.grid(row=2, column=1, sticky=NSEW)
    lblbnasc2M = tb.DateEntry(nsc2M.dentro)
    lblbnasc2M.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblbnasc2M.entry.delete(0,END)

    pare2M = Bframe(p4l3)
    pare2M.grid(row=2, column=2, sticky=NSEW)
    lblbpare2M = tb.Entry(pare2M.dentro)
    lblbpare2M.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    part2M = Bframe(p4l3)
    part2M.grid(row=2, column=3, sticky=NSEW)
    lblbpart2M = tb.Entry(part2M.dentro)
    lblbpart2M.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)


    nc3M = Bframe(p4l3)
    nc3M.grid(row=3, column=0, sticky=NSEW)
    lblbnome3M = tb.Entry(nc3M.dentro, width=50)
    lblbnome3M.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)
    
    nsc3M = Bframe(p4l3)
    nsc3M.grid(row=3, column=1, sticky=NSEW)
    lblbnasc3M = tb.DateEntry(nsc3M.dentro)
    lblbnasc3M.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblbnasc3M.entry.delete(0,END)

    pare3M = Bframe(p4l3)
    pare3M.grid(row=3, column=2, sticky=NSEW)
    lblbpare3M = tb.Entry(pare3M.dentro)
    lblbpare3M.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    part3M = Bframe(p4l3)
    part3M.grid(row=3, column=3, sticky=NSEW)
    lblbpart3M = tb.Entry(part3M.dentro)
    lblbpart3M.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    nc4M = Bframe(p4l3)
    nc4M.grid(row=4, column=0, sticky=NSEW)
    lblbnome4M = tb.Entry(nc4M.dentro, width=50)
    lblbnome4M.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)
    
    nsc4M = Bframe(p4l3)
    nsc4M.grid(row=4, column=1, sticky=NSEW)
    lblbnasc4M = tb.DateEntry(nsc4M.dentro)
    lblbnasc4M.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    lblbnasc4M.entry.delete(0,END)

    pare4M = Bframe(p4l3)
    pare4M.grid(row=4, column=2, sticky=NSEW)
    lblbpare4M = tb.Entry(pare4M.dentro)
    lblbpare4M.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    part4M = Bframe(p4l3)
    part4M.grid(row=4, column=3, sticky=NSEW)
    lblbpart4M = tb.Entry(part4M.dentro)
    lblbpart4M.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    
    frameppe = Bframe(p4l3)
    frameppe.grid(row=5, column=2, sticky=NSEW, pady=15)
    ppe = Lcheck(frameppe.dentro, texto='Pessoa Politicamente Exposta')
    ppe.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    
    titmat = Lcampo(p4l3, texto='Titular da Matrícula')
    titmat.grid(row=5, column=0, pady=15, sticky=NSEW)

    mattit = Lcampo(p4l3, texto='Matrícula')
    mattit.grid(row=5, column=1, pady=15, sticky=NSEW)

    

    
    sit_reint.var.set(1)
    if valores[1]['vida1P']: vg1.var.set(1)
    if valores[1]['vida2P']: vg2.var.set(1)
    if valores[1]['mulherP']: vg3.var.set(1)
    if valores[1]['funeralP']: af.var.set(1)
    cpo_prop.campo.insert(0, valores[0]['nome'])
    cpo_nasc.campo.entry.insert(0, valores[0]['nascimento'])
    cpo_idade.campo.insert(0, valores[0]['idade'])
    cpo_cpf.campo.insert(0, valores[0]['cpf'])
    cpo_rg.campo.insert(0, valores[0]['rg'])
    cpo_rgexp.campo.insert(0, valores[0]['orgao'])
    cpo_emiss.campo.entry.insert(0, valores[0]['expedicao'])
    if valores[0]['sexo'] == 'Masculino':
        masc.var.set(1)
    else:
        fem.var.set(1)
    cpo_estcivil.campo.insert(0, valores[0]['estadocivil'])
    cpo_ocupacao.campo.insert(0, valores[0]['funcao'])
    cpo_matricula.campo.insert(0, str(valores[0]['matricula']).split('.')[0])
    cpo_localizador.campo.insert(0, valores[0]['localizador'])
    cpo_email.campo.insert(0, valores[0]['email'])
    cpo_rota.campo.insert(0, valores[0]['rota'])
    cpo_endereco.campo.insert(0, valores[0]['logradouro'])
    cpo_numero.campo.insert(0, valores[0]['numero'])
    cpo_compl.campo.insert(0, valores[0]['complemento'])
    cpo_bairro.campo.insert(0, valores[0]['bairro'])
    cpo_cidade.campo.insert(0, valores[0]['cidade'])
    cpo_uf.campo.insert(0, valores[0]['uf'])
    cpo_cep.campo.insert(0, valores[0]['cep'])
    cpo_tel.campo.insert(0, valores[0]['telefone'])
    cpo_emailp.campo.insert(0, valores[0]['email'])
    cpo_celular.campo.insert(0, valores[0]['celulares'])
    cpo_whats.campo.insert(0, valores[0]['celulares'])
    cpo_conjuge.campo.insert(0, valores[0]['conjuge'])
    cpo_nascimentoconj.campo.entry.insert(0, valores[0]['nascimentoconjuge'])
    cpo_idadeconj.campo.insert(0, valores[0]['idadeconjuge'])
    cpo_cpfconj.campo.insert(0, valores[0]['cpfconjuge'])

    
    lblvct1.insert(0,valores[1]['vida1T'])
    lblvcc1.insert(0,valores[1]['vida1C'])
    lblvt1.insert(0,valores[1]['vida1P'])
    
    lblvct2.insert(0,valores[1]['vida2T'])
    lblvcc2.insert(0,valores[1]['vida2C'])
    lblvt2.insert(0,valores[1]['vida2P'])
    
    lblvct3.insert(0,valores[1]['mulherT'])
    lblvt3.insert(0,valores[1]['mulherP'])
    
    '''lblvct4.insert(0,valores[1]['funeralT'])
    lblvt4.insert(0,valores[1]['funeralP'])'''
    pmt.insert(0,valores[1]['total'])

    if valores[2]:
        lenvida = len(valores[2]['vida'])
        lenmulher = len(valores[2]['mulher'])
        if lenvida >= 1:
            lblbnome1.insert(0,valores[2]['vida'][0]['nome'])
            lblbnasc1.entry.insert(0,valores[2]['vida'][0]['nascimento'])
            #lblbpare1.insert(0,valores[2]['vida'][0]['parentesco'])
            lblbpart1.insert(0,valores[2]['vida'][0]['percentual'])
        if lenvida >= 2:
            lblbnome2.insert(0,valores[2]['vida'][1]['nome'])
            lblbnasc2.entry.insert(0,valores[2]['vida'][1]['nascimento'])
            lblbpare2.insert(0,valores[2]['vida'][1]['parentesco'])
            lblbpart2.insert(0,valores[2]['vida'][1]['percentual'])
        if lenvida >= 3:
            lblbnome3.insert(0,valores[2]['vida'][2]['nome'])
            lblbnasc3.entry.insert(0,valores[2]['vida'][2]['nascimento'])
            lblbpare3.insert(0,valores[2]['vida'][2]['parentesco'])
            lblbpart3.insert(0,valores[2]['vida'][2]['percentual'])
        if lenvida >= 4:
            lblbnome4.insert(0,valores[2]['vida'][3]['nome'])
            lblbnasc4.entry.insert(0,valores[2]['vida'][3]['nascimento'])
            lblbpare4.insert(0,valores[2]['vida'][3]['parentesco'])
            lblbpart4.insert(0,valores[2]['vida'][3]['percentual'])
        
        if lenmulher >= 1:
            lblbnome1M.insert(0,valores[2]['mulher'][0]['nome'])
            lblbnasc1M.entry.insert(0,valores[2]['mulher'][0]['nascimento'])
            lblbpare1M.insert(0,valores[2]['mulher'][0]['parentesco'])
            lblbpart1M.insert(0,valores[2]['mulher'][0]['percentual'])
        
        if lenmulher >= 2:
            lblbnome2M.insert(0,valores[2]['mulher'][1]['nome'])
            lblbnasc2M.entry.insert(0,valores[2]['mulher'][1]['nascimento'])
            lblbpare2M.insert(0,valores[2]['mulher'][1]['parentesco'])
            lblbpart2M.insert(0,valores[2]['mulher'][1]['percentual'])
        
        if lenmulher >= 3:
            lblbnome3M.insert(0,valores[2]['mulher'][2]['nome'])
            lblbnasc3M.entry.insert(0,valores[2]['mulher'][2]['nascimento'])
            lblbpare3M.insert(0,valores[2]['mulher'][2]['parentesco'])
            lblbpart3M.insert(0,valores[2]['mulher'][2]['percentual'])
        
        if lenmulher >= 3:
            lblbnome3M.insert(0,valores[2]['mulher'][3]['nome'])
            lblbnasc3M.entry.insert(0,valores[2]['mulher'][3]['nascimento'])
            lblbpare3M.insert(0,valores[2]['mulher'][3]['parentesco'])
            lblbpart3M.insert(0,valores[2]['mulher'][3]['percentual'])
        
    titmat.campo.insert(0,valores[0]['nome'])
    mattit.campo.insert(0,valores[0]['matricula'])
        
    def gera_proposta():
        valoresAtuais = {
            'cpo_vigenciade':cpo_vigenciade.campo.entry.get(),
            'cpo_vigenciaate':cpo_vigenciade.campo.entry.get(),
            'cpo_sub':cpo_sub.campo.get(),
            'cpo_subcod': cpo_subcod.campo.get(),
            'cpo_angcod': cpo_angcod.campo.get(),
            'cpo_proposta': cpo_proposta.campo.get(),
            'sit_ativo': sit_ativo.var.get(),
            'sit_inativo': sit_inativo.var.get(),
            'sit_reint': sit_reint.var.get(),
            'vg1': vg1.var.get(),
            'vg2': vg2.var.get(),
            'vg3': vg3.var.get(),
            'af': af.var.get(),
            'cpo_prop': cpo_prop.campo.get(),
            'cpo_nasc': cpo_nasc.campo.entry.get(),
            'cpo_idade': cpo_idade.campo.get(),
            'cpo_cpf': cpo_cpf.campo.get(),
            'cpo_rg': cpo_rg.campo.get(),
            'cpo_rgexp': cpo_rgexp.campo.get(),
            'cpo_emiss': cpo_emiss.campo.entry.get(),
            'masc': masc.var.get(),
            'fem': fem.var.get(),
            'cpo_estcivil': cpo_estcivil.campo.get(),
            'cpo_ocupacao': cpo_ocupacao.campo.get(),
            'cpo_matricula': cpo_matricula.campo.get(),
            'cpo_localizador': cpo_localizador.campo.get(),
            'cpo_email': cpo_email.campo.get(),
            'cpo_rota': cpo_rota.campo.get(),
            'cpo_endereco': cpo_endereco.campo.get(),
            'cpo_numero': cpo_numero.campo.get(),
            'cpo_compl': cpo_compl.campo.get(),
            'cpo_bairro': cpo_bairro.campo.get(),
            'cpo_cidade': cpo_cidade.campo.get(),
            'cpo_uf': cpo_uf.campo.get(),
            'cpo_cep': cpo_cep.campo.get(),
            'cpo_tel': cpo_tel.campo.get(),
            'cpo_emailp': cpo_emailp.campo.get(),
            'cpo_celular': cpo_celular.campo.get(),
            'cpo_whats': cpo_whats.campo.get(),
            'cpo_conjuge': cpo_conjuge.campo.get(),
            'cpo_nascimentoconj': cpo_nascimentoconj.campo.entry.get(),
            'cpo_idadeconj': cpo_idadeconj.campo.get(),
            'cpo_cpfconj': cpo_cpfconj.campo.get(),
            'lbltit1': lbltit1.get(),
            'lblconj1': lblconj1.get(),
            'lblvct1': lblvct1.get(),
            'lblvcc1': lblvcc1.get(),
            'lblvt1': lblvt1.get(),
            'lbltit2': lbltit2.get(),
            'lblconj2': lblconj2.get(),
            'lblvct2': lblvct2.get(),
            'lblvcc2': lblvcc2.get(),
            'lblvt2': lblvt2.get(),
            'lbltit3': lbltit3.get(),
            'lblconj3': lblconj3.get(),
            'lblvct3': lblvct3.get(),
            'lblvt3': lblvt3.get(),
            #'lbltit4': lbltit4.get(),
            #'lblconj4': lblconj4.get(),
            #'lblvct4': lblvct4.get(),
            #'lblvt4': lblvt4.get(),
            'pmt': pmt.get(),
            'lblbnome1': lblbnome1.get(),
            'lblbnasc1': lblbnasc1.entry.get(),
            'lblbpare1': lblbpare1.get(),
            'lblbpart1': lblbpart1.get(),
            'lblbnome2': lblbnome2.get(),
            'lblbnasc2': lblbnasc2.entry.get(),
            'lblbpare2': lblbpare2.get(),
            'lblbpart2': lblbpart2.get(),
            'lblbnome3': lblbnome3.get(),
            'lblbnasc3': lblbnasc3.entry.get(),
            'lblbpare3': lblbpare3.get(),
            'lblbpart3': lblbpart3.get(),
            'lblbnome4': lblbnome4.get(),
            'lblbnasc4': lblbnasc4.entry.get(),
            'lblbpare4': lblbpare4.get(),
            'lblbpart4': lblbpart4.get(),
            'lblbnome1M': lblbnome1M.get(),
            'lblbnasc1M': lblbnasc1M.entry.get(),
            'lblbpare1M': lblbpare1M.get(),
            'lblbpart1M': lblbpart1M.get(),
            'lblbnome2M': lblbnome2M.get(),
            'lblbnasc2M': lblbnasc2M.entry.get(),
            'lblbpare2M': lblbpare2M.get(),
            'lblbpart2M': lblbpart2M.get(),
            'lblbnome3M': lblbnome3M.get(),
            'lblbnasc3M': lblbnasc3M.entry.get(),
            'lblbpare3M': lblbpare3M.get(),
            'lblbpart3M': lblbpart3M.get(),
            'lblbnome4M': lblbnome4M.get(),
            'lblbnasc4M': lblbnasc4M.entry.get(),
            'lblbpare4M': lblbpare4M.get(),
            'lblbpart4M': lblbpart4M.get(),
            'ppe':ppe.var.get(),
            'titmat':titmat.campo.get(),
            'mattit':mattit.campo.get(),
        }
        if pdf(valoresAtuais):
            telatop.destroy()
        else:
            dialogs.Messagebox.show_error('Erro ao gerar o PDF.')

    def cancela():
        telatop.destroy()
        

    parte5 = tb.Frame(stage)
    parte5.grid(padx=10, sticky=EW)
    l1p5 = tb.Frame(parte5)
    l1p5.grid(sticky=EW)
    gravar = tb.Button(l1p5, text='Gerar PDF', command=gera_proposta, width=15)
    gravar.grid(row=0, column=0, padx=10, pady=10)
    cancelar = tb.Button(l1p5, text='Cancelar', command=cancela, width=15)
    cancelar.grid(row=0, column=1, padx=10, pady=10)
