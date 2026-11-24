"""Biblioteca mínima de pixel art em SVG para o README de perfil.

Tudo é desenhado com <rect>: fonte bitmap 5x7 própria (com acentos),
sprites por matriz de caracteres, barras segmentadas e molduras.
Sem fontes externas, sem scripts: só o que o GitHub renderiza em <img>.
"""

# ---------------------------------------------------------------- paleta
PINK = "#FF009B"
PINK_DK = "#B8006F"
NAVY = "#192D37"
NAVY_DK = "#0E1A21"
BLUE = "#1F4FBF"
CYAN = "#3DF2FF"
LIME = "#9BFF3D"
YELLOW = "#FFD23D"
ORANGE = "#FF8A3D"
RED = "#FF3D5A"
WHITE = "#F4F4F4"
GREY = "#8A9BA8"
GREY_DK = "#3C4C57"
BLACK = "#07090C"
CREAM = "#EDE4CF"
SKIN = "#F2C9A0"

# ---------------------------------------------------------------- fonte 5x7
# Cada glifo: 7 linhas de 5 colunas. Acentos ocupam 2 linhas acima (cell 5x10,
# letra nas linhas 2-8, cedilha na linha 9).
GLYPHS = {
"A": ["01110","10001","10001","11111","10001","10001","10001"],
"B": ["11110","10001","10001","11110","10001","10001","11110"],
"C": ["01110","10001","10000","10000","10000","10001","01110"],
"D": ["11110","10001","10001","10001","10001","10001","11110"],
"E": ["11111","10000","10000","11110","10000","10000","11111"],
"F": ["11111","10000","10000","11110","10000","10000","10000"],
"G": ["01110","10001","10000","10111","10001","10001","01111"],
"H": ["10001","10001","10001","11111","10001","10001","10001"],
"I": ["11111","00100","00100","00100","00100","00100","11111"],
"J": ["00111","00010","00010","00010","00010","10010","01100"],
"K": ["10001","10010","10100","11000","10100","10010","10001"],
"L": ["10000","10000","10000","10000","10000","10000","11111"],
"M": ["10001","11011","10101","10101","10001","10001","10001"],
"N": ["10001","10001","11001","10101","10011","10001","10001"],
"O": ["01110","10001","10001","10001","10001","10001","01110"],
"P": ["11110","10001","10001","11110","10000","10000","10000"],
"Q": ["01110","10001","10001","10001","10101","10010","01101"],
"R": ["11110","10001","10001","11110","10100","10010","10001"],
"S": ["01111","10000","10000","01110","00001","00001","11110"],
"T": ["11111","00100","00100","00100","00100","00100","00100"],
"U": ["10001","10001","10001","10001","10001","10001","01110"],
"V": ["10001","10001","10001","10001","10001","01010","00100"],
"W": ["10001","10001","10001","10101","10101","10101","01010"],
"X": ["10001","10001","01010","00100","01010","10001","10001"],
"Y": ["10001","10001","01010","00100","00100","00100","00100"],
"Z": ["11111","00001","00010","00100","01000","10000","11111"],
"0": ["01110","10001","10011","10101","11001","10001","01110"],
"1": ["00100","01100","00100","00100","00100","00100","01110"],
"2": ["01110","10001","00001","00010","00100","01000","11111"],
"3": ["11110","00001","00001","01110","00001","00001","11110"],
"4": ["00010","00110","01010","10010","11111","00010","00010"],
"5": ["11111","10000","10000","11110","00001","00001","11110"],
"6": ["01110","10000","10000","11110","10001","10001","01110"],
"7": ["11111","00001","00010","00100","01000","01000","01000"],
"8": ["01110","10001","10001","01110","10001","10001","01110"],
"9": ["01110","10001","10001","01111","00001","00001","01110"],
" ": ["00000","00000","00000","00000","00000","00000","00000"],
".": ["00000","00000","00000","00000","00000","01100","01100"],
",": ["00000","00000","00000","00000","00110","00110","01100"],
":": ["00000","01100","01100","00000","01100","01100","00000"],
";": ["00000","01100","01100","00000","01100","01100","11000"],
"!": ["00100","00100","00100","00100","00100","00000","00100"],
"?": ["01110","10001","00001","00110","00100","00000","00100"],
"-": ["00000","00000","00000","11111","00000","00000","00000"],
"_": ["00000","00000","00000","00000","00000","00000","11111"],
"/": ["00001","00010","00010","00100","01000","01000","10000"],
"(": ["00010","00100","01000","01000","01000","00100","00010"],
")": ["01000","00100","00010","00010","00010","00100","01000"],
"[": ["01110","01000","01000","01000","01000","01000","01110"],
"]": ["01110","00010","00010","00010","00010","00010","01110"],
"<": ["00010","00100","01000","10000","01000","00100","00010"],
">": ["01000","00100","00010","00001","00010","00100","01000"],
"+": ["00000","00100","00100","11111","00100","00100","00000"],
"=": ["00000","00000","11111","00000","11111","00000","00000"],
"'": ["00100","00100","01000","00000","00000","00000","00000"],
'"': ["01010","01010","10100","00000","00000","00000","00000"],
"#": ["01010","01010","11111","01010","11111","01010","01010"],
"%": ["11001","11010","00010","00100","01000","01011","10011"],
"&": ["01100","10010","10100","01000","10101","10010","01101"],
"*": ["00000","10101","01110","11111","01110","10101","00000"],
"@": ["01110","10001","10111","10101","10111","10000","01110"],
"|": ["00100","00100","00100","00100","00100","00100","00100"],
"♥": ["01010","11111","11111","11111","01110","00100","00000"],
"★": ["00100","00100","11111","01110","01110","11011","00000"],
"→": ["00000","00100","00010","11111","00010","00100","00000"],
"✓": ["00000","00001","00010","10100","01000","00000","00000"],
"▶": ["10000","11000","11100","11110","11100","11000","10000"],
"░": ["10101","01010","10101","01010","10101","01010","10101"],
"█": ["11111","11111","11111","11111","11111","11111","11111"],
"·": ["00000","00000","00000","01100","01100","00000","00000"],
"º": ["01110","01010","01110","00000","00000","00000","00000"],
}
# acentos: (base, desenho de 2 linhas acima)
ACCENTS = {
    "Á": ("A", ["00010", "00100"]), "É": ("E", ["00010", "00100"]),
    "Í": ("I", ["00010", "00100"]), "Ó": ("O", ["00010", "00100"]),
    "Ú": ("U", ["00010", "00100"]),
    "À": ("A", ["01000", "00100"]),
    "Â": ("A", ["00100", "01010"]), "Ê": ("E", ["00100", "01010"]),
    "Ô": ("O", ["00100", "01010"]),
    "Ã": ("A", ["01101", "10110"]), "Õ": ("O", ["01101", "10110"]),
}
CEDILLA = {"Ç": "C"}

CELL_W, CELL_H = 5, 10  # 2 linhas de acento + 7 de letra + 1 de cedilha


def glyph_rows(ch):
    """Retorna 10 linhas de 5 colunas para o caractere (maiúsculo)."""
    ch = ch.upper()
    blank = "00000"
    if ch in ACCENTS:
        base, acc = ACCENTS[ch]
        return acc + GLYPHS[base] + [blank]
    if ch in CEDILLA:
        return [blank, blank] + GLYPHS[CEDILLA[ch]] + ["00110"]
    g = GLYPHS.get(ch, GLYPHS["?"])
    return [blank, blank] + g + [blank]


def text_width(s, px=3, spacing=1):
    return len(s) * (CELL_W + spacing) * px - spacing * px


def _runs(row):
    """Agrupa colunas acesas em runs (início, comprimento)."""
    out, start = [], None
    for i, c in enumerate(row + "0"):
        if c == "1" and start is None:
            start = i
        elif c != "1" and start is not None:
            out.append((start, i - start))
            start = None
    return out


def text(x, y, s, color=WHITE, px=3, spacing=1, extra=""):
    """Texto em pixel. y é o topo da célula (inclui as 2 linhas de acento)."""
    parts = []
    cx = x
    for ch in s:
        rows = glyph_rows(ch)
        for r, row in enumerate(rows):
            for start, length in _runs(row):
                parts.append(
                    f'<rect x="{cx + start * px}" y="{y + r * px}" '
                    f'width="{length * px}" height="{px}" fill="{color}"{extra}/>'
                )
        cx += (CELL_W + spacing) * px
    return "".join(parts)


def text_centered(cx, y, s, color=WHITE, px=3, spacing=1, extra=""):
    return text(cx - text_width(s, px, spacing) // 2, y, s, color, px, spacing, extra)


def sprite(x, y, rows, palette, px=4):
    """Matriz de caracteres → rects. '.' é transparente."""
    parts = []
    for r, row in enumerate(rows):
        c = 0
        while c < len(row):
            ch = row[c]
            if ch == ".":
                c += 1
                continue
            start = c
            while c < len(row) and row[c] == ch:
                c += 1
            parts.append(
                f'<rect x="{x + start * px}" y="{y + r * px}" '
                f'width="{(c - start) * px}" height="{px}" fill="{palette[ch]}"/>'
            )
    return "".join(parts)


def frame(x, y, w, h, px=4, fill=NAVY_DK, border=WHITE, inner=GREY_DK, notch=True):
    """Moldura dupla estilo caixa de diálogo de RPG (cantos chanfrados)."""
    p = []
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>')
    # borda externa (1 px) com cantos vazados
    p.append(f'<rect x="{x + px}" y="{y}" width="{w - 2 * px}" height="{px}" fill="{border}"/>')
    p.append(f'<rect x="{x + px}" y="{y + h - px}" width="{w - 2 * px}" height="{px}" fill="{border}"/>')
    p.append(f'<rect x="{x}" y="{y + px}" width="{px}" height="{h - 2 * px}" fill="{border}"/>')
    p.append(f'<rect x="{x + w - px}" y="{y + px}" width="{px}" height="{h - 2 * px}" fill="{border}"/>')
    # borda interna (1 px) deslocada 2 px
    o = 2 * px
    p.append(f'<rect x="{x + o}" y="{y + o}" width="{w - 2 * o}" height="{px}" fill="{inner}"/>')
    p.append(f'<rect x="{x + o}" y="{y + h - o - px}" width="{w - 2 * o}" height="{px}" fill="{inner}"/>')
    p.append(f'<rect x="{x + o}" y="{y + o}" width="{px}" height="{h - 2 * o}" fill="{inner}"/>')
    p.append(f'<rect x="{x + w - o - px}" y="{y + o}" width="{px}" height="{h - 2 * o}" fill="{inner}"/>')
    if notch:
        for nx, ny in ((x + px, y + px), (x + w - 2 * px, y + px), (x + px, y + h - 2 * px), (x + w - 2 * px, y + h - 2 * px)):
            p.append(f'<rect x="{nx}" y="{ny}" width="{px}" height="{px}" fill="{border}"/>')
    return "".join(p)


def bar(x, y, w, h, pct, fg=LIME, bg=GREY_DK, px=4, segments=None, shade=None):
    """Barra segmentada (HP/XP). pct em 0..1."""
    p = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{BLACK}"/>']
    ix, iy, iw, ih = x + px, y + px, w - 2 * px, h - 2 * px
    p.append(f'<rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" fill="{bg}"/>')
    if segments:
        seg_w = iw // segments
        lit = round(pct * segments)
        for i in range(segments):
            sx = ix + i * seg_w
            if i < lit:
                p.append(f'<rect x="{sx}" y="{iy}" width="{seg_w - px}" height="{ih}" fill="{fg}"/>')
                if shade:
                    p.append(f'<rect x="{sx}" y="{iy + ih - px}" width="{seg_w - px}" height="{px}" fill="{shade}"/>')
    else:
        fw = int(iw * pct) // px * px
        p.append(f'<rect x="{ix}" y="{iy}" width="{fw}" height="{ih}" fill="{fg}"/>')
        if shade and fw:
            p.append(f'<rect x="{ix}" y="{iy + ih - px}" width="{fw}" height="{px}" fill="{shade}"/>')
            p.append(f'<rect x="{ix}" y="{iy}" width="{fw}" height="{px}" fill="{WHITE}" opacity="0.35"/>')
    return "".join(p)


def scanlines(w, h, opacity=0.12):
    return (
        f'<defs><pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">'
        f'<rect width="4" height="2" fill="#000" opacity="{opacity}"/></pattern></defs>'
        f'<rect width="{w}" height="{h}" fill="url(#scan)"/>'
    )


def blink(dur="1.2s", values="1;1;0;0"):
    return f'<animate attributeName="opacity" values="{values}" dur="{dur}" repeatCount="indefinite"/>'


def svg(w, h, body, bg=None, title=""):
    bgrect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    t = f"<title>{title}</title>" if title else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" shape-rendering="crispEdges">{t}{bgrect}{body}</svg>'
    )


# ---------------------------------------------------------------- sprites
CHAR_PAL = {
    "h": "#1B1F2A", "s": SKIN, "e": "#1B1F2A", "m": "#C2775C", "H": CYAN, "p": PINK,
    "d": PINK_DK, "n": NAVY, "k": "#1B1F2A", "w": WHITE, "b": BLUE, "g": "#5A6B78",
}
# 16 x 22
CHARACTER = [
    "......hhhh......",
    "....hhhhhhhh....",
    "...hhhhhhhhhh...",
    "..HhhhhhhhhhhH..",
    "..HhsssssssshH..",
    "..HsseesseessH..",
    "..HssssssssssH..",
    "...ssssmmssss...",
    "....ssssssss....",
    ".....pppppp.....",
    "...pppppppppp...",
    "..ppppddddpppp..",
    "..pppdwwwwdppp..",
    ".sppppddddpppps.",
    ".sppppppppppppps",
    "..ddpppppppppdd.",
    "...nnnnnnnnnn...",
    "...nnnn..nnnn...",
    "...nnnn..nnnn...",
    "...nnnn..nnnn...",
    "..kkkkk..kkkkk..",
    "..kkkkk..kkkkk..",
]

ICON_PAL = {
    "r": RED, "R": "#B8142F", "y": YELLOW, "Y": "#C99A12", "c": CYAN, "C": "#1A9FB0",
    "w": WHITE, "g": GREY, "G": GREY_DK, "l": LIME, "L": "#5FAE1E", "p": PINK, "P": PINK_DK,
    "b": BLUE, "B": "#143483", "o": ORANGE, "k": BLACK, "n": NAVY, "s": SKIN,
}
ICONS = {
    "heart": [
        "........",
        ".rr..rr.",
        "rwrrrrrr",
        "rrrrrrrr",
        "RrrrrrrR",
        ".RrrrrR.",
        "..RrrR..",
        "...RR...",
    ],
    "heart_empty": [
        "........",
        ".GG..GG.",
        "G..GG..G",
        "G......G",
        "G......G",
        ".G....G.",
        "..G..G..",
        "...GG...",
    ],
    "bolt": [
        "....yy..",
        "...yyy..",
        "..yyy...",
        ".yyyyyy.",
        "..Yyyy..",
        "..Yyy...",
        ".Yy.....",
        "Y.......",
    ],
    "coin": [
        "..yyyy..",
        ".yYYYYy.",
        "yYwYYYYy",
        "yYwYYYYy",
        "yYYYYYYy",
        "yYYYYYYy",
        ".yYYYYy.",
        "..yyyy..",
    ],
    "sword": [
        ".......c",
        "......cw",
        ".....cw.",
        "....cw..",
        "y..cw...",
        ".yyw....",
        "..yy....",
        ".y..y...",
    ],
    "shield": [
        "bbbbbbbb",
        "bwwbbbbb",
        "bwbbbbbb",
        "bbbbbbbb",
        "BbbbbbbB",
        ".BbbbbB.",
        "..BbbB..",
        "...BB...",
    ],
    "potion": [
        "...gg...",
        "...gg...",
        "..gwwg..",
        ".gppppg.",
        "gpwppppg",
        "gppppppg",
        "gPppppPg",
        ".gPPPPg.",
    ],
    "gear": [
        "..g..g..",
        ".gggggg.",
        "gggwwggg",
        ".ggwwgg.",
        ".ggwwgg.",
        "gggwwggg",
        ".gggggg.",
        "..g..g..",
    ],
    "cloud": [
        "........",
        "...www..",
        "..wwwww.",
        ".wwwwwww",
        "wwwwwwww",
        "wwwwwwww",
        ".gggggg.",
        "........",
    ],
    "db": [
        ".cccccc.",
        "cCCCCCCc",
        ".cccccc.",
        "cCCCCCCc",
        ".cccccc.",
        "cCCCCCCc",
        ".cccccc.",
        "........",
    ],
    "star": [
        "...yy...",
        "...yy...",
        "yyyyyyyy",
        ".yyyyyy.",
        "..yyyy..",
        ".yyYYyy.",
        "yy....yy",
        "........",
    ],
    "pad": [
        "........",
        ".gggggg.",
        "gwgggggg",
        "gwwwgrgg",
        "gwgggggg",
        "gggggggg",
        ".gg..gg.",
        "........",
    ],
    "floppy": [
        "nnnnnnn.",
        "nwwwwwnn",
        "nwwwwwnn",
        "nnnnnnnn",
        "nnnnnnnn",
        "nnwwwwnn",
        "nnwwwwnn",
        "nnnnnnnn",
    ],
    "scroll": [
        "ssssssss",
        "ss....ss",
        "s.gggg.s",
        "s......s",
        "s.gggg.s",
        "s......s",
        "s.ggg..s",
        "ssssssss",
    ],
    "key": [
        ".....yy.",
        "....yYYy",
        "....yYYy",
        "...yyyy.",
        "..yy....",
        ".yy.....",
        "yyy.....",
        "y.y.....",
    ],
    "flag": [
        "p.......",
        "pppppp..",
        "pwwpppp.",
        "pppppppp",
        "ppppppp.",
        "pppppp..",
        "p.......",
        "p.......",
    ],
    "skull": [
        "..wwww..",
        ".wwwwww.",
        "wwkwwkww",
        "wwkwwkww",
        "wwwwwwww",
        ".wwkkww.",
        "..wwww..",
        "..w.w.w.",
    ],
}


def icon(name, x, y, px=3):
    return sprite(x, y, ICONS[name], ICON_PAL, px)


def hearts(x, y, full, total, px=3, gap=4):
    out = []
    for i in range(total):
        out.append(icon("heart" if i < full else "heart_empty", x + i * (8 * px + gap), y, px))
    return "".join(out)
