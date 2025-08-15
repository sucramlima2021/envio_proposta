# merge_overlay.py
from io import BytesIO
from pypdf import PdfReader, PdfWriter

def mesclar_template(template_pdf_path, overlay_bytesio, saida_path):
    bg = PdfReader(template_pdf_path)             # fundo (seu PDF nítido)
    ov = PdfReader(overlay_bytesio)               # overlay em memória
    out = PdfWriter()

    # Se os tamanhos de página forem iguais (esperado), é só mesclar
    for i, bg_pg in enumerate(bg.pages):
        if i < len(ov.pages):
            bg_pg.merge_page(ov.pages[i])
        out.add_page(bg_pg)

    with open(saida_path, "wb") as f:
        out.write(f)
