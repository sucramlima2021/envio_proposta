# overlay_helpers.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

PAGE_W, PAGE_H = A4  # 595 x 842 pt (1pt = 1/72in)

def reg_font_kartika(path):
    try:
        pdfmetrics.getFont(path)
    except KeyError:
        pdfmetrics.registerFont(TTFont('Kartika', path))

def mm_to_pt(x_mm, y_mm):
    return x_mm * mm, y_mm * mm

def tl_to_rl(x_mm, y_mm):
    """Converte coordenada a partir do canto superior-esquerdo (top-left, em mm)
       para o sistema do ReportLab (bottom-left, em pt)."""
    x_pt, y_pt = mm_to_pt(x_mm, y_mm)
    return x_pt, PAGE_H - y_pt

def draw_text(c, x_mm, y_mm, text, size=9, font="Kartika", align="left", max_width=None):
    x, y_from_top = mm_to_pt(x_mm, y_mm)
    x_pt, y_pt = x, PAGE_H - y_from_top
    c.setFont(font, size)
    s = str(text) if text is not None else ""
    if align == "left":
        c.drawString(x_pt, y_pt, s)
    elif align == "center":
        w = pdfmetrics.stringWidth(s, font, size)
        c.drawString(x_pt - w/2, y_pt, s)
    elif align == "right":
        w = pdfmetrics.stringWidth(s, font, size)
        c.drawString(x_pt - w, y_pt, s)
    else:
        c.drawString(x_pt, y_pt, s)

def draw_checkbox(c, x_mm, y_mm, size_mm=4, checked=False):
    size_pt = size_mm * mm
    x_pt, y_pt = tl_to_rl(x_mm, y_mm + size_mm)  # y_mm dado como topo da caixinha
    c.rect(x_pt, y_pt, size_pt, size_pt, stroke=1, fill=0)
    if checked:
        # X simples
        c.setLineWidth(1)
        c.line(x_pt + 1, y_pt + 1, x_pt + size_pt - 1, y_pt + size_pt - 1)
        c.line(x_pt + 1, y_pt + size_pt - 1, x_pt + size_pt - 1, y_pt + 1)
