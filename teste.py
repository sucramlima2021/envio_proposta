from PyPDF2 import PdfReader, PdfWriter

A4_W, A4_H = 595, 842
r = PdfReader("proposta_reintegracao.pdf")
w = PdfWriter()

for p in r.pages:
    p.scale_to(A4_W, A4_H)   # estica X e Y para caber exatamente
    w.add_page(p)

with open("proposta_A4_stretched.pdf", "wb") as f:
    w.write(f)