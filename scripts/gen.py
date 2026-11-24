"""Gera os SVGs do README de perfil em ../assets.

Uso: python3 -I scripts/gen.py [--only m2]
Os números do placar vêm das variáveis de ambiente PRS_MERGED, COMMITS e
DATA (dd.mm.aaaa); sem elas, valem os últimos valores conhecidos abaixo.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pixel import *  # noqa

OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(OUT, exist_ok=True)
W = 880  # largura do README no GitHub

# -------------------------------------------------------------- dados reais
NAME = "GABRIEL JESUS"
CLASSE = "SOLUTIONS ENGINEER"
GUILDA = "PAGALEVE"
SEMESTRE = 8  # Eng. da Computação, 8º semestre
PRS_MERGED = int(os.environ.get("PRS_MERGED", 69))   # PRs mergeadas (search API, inclui repos privados)
COMMITS = int(os.environ.get("COMMITS", 101))         # commits (search API)
DATA = os.environ.get("DATA", "09.11.2026")

TECHS = [  # (nome, categoria, ícone)
    ("NODE.JS", "BACK-END", "gear"), ("NESTJS", "BACK-END", "gear"), ("RUST", "BACK-END", "gear"),
    ("AWS LAMBDA", "CLOUD", "cloud"), ("DYNAMODB", "CLOUD", "db"), ("CLOUDWATCH", "CLOUD", "cloud"),
    ("PULUMI", "INFRA", "key"), ("SNOWFLAKE", "DADOS", "db"), ("METABASE", "DADOS", "db"),
    ("N8N", "AUTOMAÇÃO", "bolt"), ("CLAUDE CODE", "IA", "star"), ("POSTMAN", "APIS", "sword"),
]
ATRIBUTOS = [  # flavor de ficha: as áreas reais da bio
    ("INTEGRAÇÕES", 0.9, PINK), ("AUTOMAÇÃO", 0.8, CYAN), ("INCIDENTES", 0.8, RED),
    ("DADOS", 0.6, BLUE), ("DIPLOMACIA", 0.9, YELLOW), ("CÓDIGO", 0.7, LIME),
]


def save(name, content):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{name:28s} {os.path.getsize(path):>7d} bytes")


# ============================================================== MODELO 1: RPG
def m1_header():
    h = 268
    b = [frame(0, 0, W, h, px=4, fill=NAVY_DK, border=WHITE, inner=PINK)]
    # pedestal + sprite
    b.append(f'<rect x="40" y="226" width="136" height="12" fill="{GREY_DK}"/>')
    b.append(f'<rect x="48" y="238" width="120" height="6" fill="{BLACK}"/>')
    b.append(sprite(60, 94, CHARACTER, CHAR_PAL, px=6))
    # brilho piscando atrás do personagem (aura)
    b.append(f'<g>{blink("2.4s", "0.15;0.45;0.15")}<rect x="52" y="84" width="112" height="4" fill="{PINK}"/>'
             f'<rect x="44" y="88" width="128" height="4" fill="{PINK}" opacity="0.5"/></g>')
    # nome e classe
    x = 220
    b.append(text(x, 28, NAME, WHITE, px=5))
    b.append(text(x, 88, CLASSE, PINK, px=3))
    b.append(text(x + text_width(CLASSE, 3) + 16, 88, f"· GUILDA {GUILDA}", GREY, px=3))
    # nível
    b.append(text(x, 124, f"LV {SEMESTRE:02d}", YELLOW, px=3))
    b.append(text(x + 120, 124, "ENG. DA COMPUTAÇÃO", GREY, px=3))
    # barras
    def row(y, label, pct, fg, shade, legend):
        b.append(text(x, y, label, WHITE, px=3))
        b.append(bar(x + 60, y - 2, 360, 24, pct, fg=fg, px=4, shade=shade))
        b.append(text(x + 432, y, legend, GREY, px=3))
    row(160, "HP", 1.0, LIME, "#5FAE1E", "100/100")
    row(194, "MP", 0.85, CYAN, "#1A9FB0", "CAFÉ 85%")
    row(228, "XP", SEMESTRE / 10, YELLOW, "#C99A12", f"{SEMESTRE}/10 SEM")
    # corações no canto
    b.append(hearts(W - 40 - 5 * 28, 24, 5, 5, px=3))
    b.append(text(W - 40 - text_width("PLENO", 3), 60, "PLENO", PINK, px=3))
    save("m1-header.svg", svg(W, h, "".join(b), title="Ficha de personagem: Gabriel Jesus, Solutions Engineer"))


def m1_atributos():
    w, h = 428, 272
    b = [frame(0, 0, w, h, px=4, fill=NAVY_DK, border=WHITE, inner=GREY_DK)]
    b.append(text(24, 22, "ATRIBUTOS", PINK, px=3))
    y = 60
    for label, pct, color in ATRIBUTOS:
        b.append(text(24, y, label, WHITE, px=2))
        b.append(bar(176, y - 4, 228, 20, pct, fg=color, px=4, segments=10))
        y += 34
    save("m1-atributos.svg", svg(w, h, "".join(b), title="Atributos"))


def m1_party():
    w, h = 428, 272
    b = [frame(0, 0, w, h, px=4, fill=NAVY_DK, border=WHITE, inner=GREY_DK)]
    b.append(text(24, 22, "PARTY (A PONTE)", PINK, px=3))
    members = [("ENGENHARIA", "gear", CYAN), ("PRODUTO", "scroll", YELLOW), ("COMERCIAL", "coin", LIME),
               ("CS", "heart", RED), ("PARCEIROS", "flag", PINK)]
    y = 60
    for name, ic, col in members:
        b.append(icon(ic, 24, y - 6, px=3))
        b.append(text(64, y, name, WHITE, px=2))
        b.append(text(260, y, "ALIADO", col, px=2))
        b.append(text(340, y, "♥♥♥", col, px=2))
        y += 40
    save("m1-party.svg", svg(w, h, "".join(b), title="Party: Engenharia, Produto, Comercial, CS e parceiros"))


def inventory(name, title, fill, border, inner, slot_fill, label_col, sub_col, accent):
    cols, slot_w, slot_h, gap = 4, 202, 60, 14
    rows = (len(TECHS) + cols - 1) // cols
    h = 60 + rows * (slot_h + gap) + 10
    b = [frame(0, 0, W, h, px=4, fill=fill, border=border, inner=inner)]
    b.append(text(24, 22, title, accent, px=3))
    b.append(text(W - 24 - text_width(f"{len(TECHS)}/{len(TECHS)} ITENS", 2), 24, f"{len(TECHS)}/{len(TECHS)} ITENS", sub_col, px=2))
    for i, (tname, cat, ic) in enumerate(TECHS):
        r, c = divmod(i, cols)
        x = 24 + c * (slot_w + gap)
        y = 58 + r * (slot_h + gap)
        b.append(f'<rect x="{x}" y="{y}" width="{slot_w}" height="{slot_h}" fill="{BLACK}"/>')
        b.append(f'<rect x="{x + 4}" y="{y + 4}" width="{slot_w - 8}" height="{slot_h - 8}" fill="{slot_fill}"/>')
        b.append(f'<rect x="{x + 4}" y="{y + 4}" width="{slot_w - 8}" height="4" fill="{WHITE}" opacity="0.08"/>')
        b.append(icon(ic, x + 14, y + 14, px=4))
        b.append(text(x + 58, y + 10, tname, label_col, px=2))
        b.append(text(x + 58, y + 34, cat, sub_col, px=2))
    save(name, svg(W, h, "".join(b), title="Inventário de tecnologias"))


def section_banner(name, title, style):
    h = 40
    if style == "rpg":
        b = [f'<rect width="{W}" height="{h}" fill="{NAVY_DK}"/>',
             f'<rect x="0" y="0" width="12" height="{h}" fill="{PINK}"/>',
             f'<rect x="0" y="{h - 4}" width="{W}" height="4" fill="{GREY_DK}"/>',
             text(28, 8, "▶ " + title, WHITE, px=3)]
    elif style == "arcade":
        b = [f'<rect width="{W}" height="{h}" fill="{BLACK}"/>',
             f'<rect x="0" y="{h - 4}" width="{W}" height="4" fill="{PINK}"/>',
             f'<rect x="0" y="{h - 8}" width="{W}" height="4" fill="{CYAN}" opacity="0.6"/>',
             text_centered(W // 2 + 3, 9, title, PINK_DK, px=3),
             text_centered(W // 2, 6, title, CYAN, px=3)]
    else:  # manual
        b = [f'<rect width="{W}" height="{h}" fill="{CREAM}"/>',
             f'<rect x="0" y="0" width="{W}" height="4" fill="{NAVY}"/>',
             f'<rect x="0" y="{h - 4}" width="{W}" height="4" fill="{NAVY}"/>',
             text(24, 8, title, NAVY, px=3),
             text(W - 24 - text_width("PGLV-001", 2), 12, "PGLV-001", PINK, px=2)]
    save(name, svg(W, h, "".join(b), title=title))


# =========================================================== MODELO 2: ARCADE
def m2_hud():
    h = 330
    b = [f'<rect width="{W}" height="{h}" fill="{BLACK}"/>']
    # grade de fundo (chão em perspectiva falsa: linhas horizontais)
    for i, y in enumerate((230, 246, 266, 290, 326)):
        b.append(f'<rect x="0" y="{y}" width="{W}" height="2" fill="{BLUE}" opacity="{0.25 + i * 0.12:.2f}"/>')
    # HUD superior
    b.append(f'<g>{blink("1s")}{text(24, 18, "1UP", CYAN, px=3)}</g>')
    b.append(text(96, 18, NAME, WHITE, px=3))
    b.append(text(W // 2 - text_width("HI-SCORE", 3) // 2, 18, "HI-SCORE", RED, px=3))
    b.append(text_centered(W // 2, 46, f"{COMMITS:07d}", WHITE, px=3))
    b.append(text(24, 46, f"{PRS_MERGED:07d}", WHITE, px=3))
    b.append(text(W - 24 - text_width("CREDIT 01", 3), 18, "CREDIT 01", YELLOW, px=3))
    b.append(hearts(W - 24 - 3 * 28, 44, 3, 3, px=3))
    # título neon com sombra dupla
    title = "SOLUTIONS ENGINEER"
    b.append(text_centered(W // 2 + 6, 96, title, PINK_DK, px=5))
    b.append(text_centered(W // 2 + 3, 93, title, BLUE, px=5))
    b.append(text_centered(W // 2, 90, title, PINK, px=5))
    b.append(text_centered(W // 2, 150, f"GUILDA {GUILDA} · FINTECH DE PAGAMENTOS", GREY, px=2))
    # press start
    b.append(f'<g>{blink("1.4s")}{text_centered(W // 2, 180, "PRESS START", WHITE, px=3)}</g>')
    # personagem e plataforma
    b.append(f'<rect x="64" y="300" width="112" height="8" fill="{GREY_DK}"/>')
    b.append(f'<rect x="64" y="300" width="112" height="2" fill="{CYAN}"/>')
    b.append(sprite(88, 212, CHARACTER, CHAR_PAL, px=4))
    # moedas e stage à direita
    b.append(icon("coin", W - 220, 214, px=3))
    b.append(text(W - 188, 216, f"x{PRS_MERGED:02d}  PRS", YELLOW, px=2))
    b.append(text(W - 220, 248, f"STAGE {SEMESTRE:02d}-1", WHITE, px=2))
    b.append(text(W - 220, 272, "ENG. COMPUTAÇÃO", GREY, px=2))
    b.append(text(24, 304, f"ATUALIZADO {DATA}", GREY_DK, px=2))
    b.append(scanlines(W, h, 0.18))
    save("m2-hud.svg", svg(W, h, "".join(b), title="Arcade: Gabriel Jesus, Solutions Engineer"))


def m2_stages():
    stages = [
        ("STAGE 1", "FLUXO CUSTOM API", "API INTERATIVA", "NOW PLAYING", LIME, "pad"),
        ("STAGE 2", "PAYMENT ICONS", "PR ACTIVEMERCHANT", "CLEAR", CYAN, "coin"),
        ("STAGE 3", "PDI PÚBLICO", "PLANO DE CARREIRA", "CLEAR", CYAN, "scroll"),
    ]
    cw, ch, gap = 272, 150, 32
    h = ch + 20
    b = [f'<rect width="{W}" height="{h}" fill="{BLACK}"/>']
    for i, (num, title, sub, status, col, ic) in enumerate(stages):
        x = 8 + i * (cw + gap)
        b.append(frame(x, 10, cw, ch, px=4, fill=NAVY_DK, border=col, inner=GREY_DK, notch=False))
        b.append(text(x + 20, 28, num, YELLOW, px=2))
        b.append(icon(ic, x + cw - 52, 24, px=3))
        b.append(text(x + 20, 56, title, WHITE, px=2))
        b.append(text(x + 20, 80, sub, GREY, px=2))
        b.append(f'<rect x="{x + 20}" y="{112}" width="{cw - 40}" height="2" fill="{GREY_DK}"/>')
        g = f'<g>{blink("1.2s") if status == "NOW PLAYING" else ""}{text(x + 20, 124, status, col, px=2)}</g>'
        b.append(g)
        b.append(text(x + cw - 20 - text_width("★★★", 2), 124, "★★★" if status == "CLEAR" else "★★░", YELLOW, px=2))
    b.append(scanlines(W, h, 0.14))
    save("m2-stages.svg", svg(W, h, "".join(b), title="Stage select: projetos"))


def m2_continue():
    h = 120
    b = [f'<rect width="{W}" height="{h}" fill="{BLACK}"/>']
    b.append(text_centered(W // 2, 20, "CONTINUE?", WHITE, px=4))
    # contagem regressiva 9..0 animada (cada dígito aparece 1s)
    for i, d in enumerate("9876543210"):
        vals = ";".join("1" if j == i else "0" for j in range(10)) + ";0"
        b.append(f'<g opacity="0"><animate attributeName="opacity" values="{vals}" keyTimes="'
                 + ";".join(f"{k / 10:.1f}" for k in range(11)) + '" dur="10s" calcMode="discrete" repeatCount="indefinite"/>'
                 + text_centered(W // 2, 64, d, PINK, px=4) + "</g>")
    b.append(f'<g>{blink("1s")}{text(24, 72, "INSERT COIN", YELLOW, px=2)}</g>')
    b.append(text(W - 24 - text_width("→ LINKEDIN / E-MAIL", 2), 72, "→ LINKEDIN / E-MAIL", CYAN, px=2))
    b.append(scanlines(W, h, 0.14))
    save("m2-continue.svg", svg(W, h, "".join(b), title="Continue? Fale comigo"))


def m2_highscore():
    rows = [
        ("1ST", "GAB", "PRS MERGED", PRS_MERGED, PINK),
        ("2ND", "GAB", "COMMITS", COMMITS, CYAN),
        ("3RD", "GAB", "STAGES CLEAR", 2, LIME),
        ("4TH", "GAB", "OPEN SOURCE PR", 1, YELLOW),
        ("5TH", "GAB", "SEMESTRES", SEMESTRE, WHITE),
    ]
    h = 70 + len(rows) * 34 + 40
    b = [f'<rect width="{W}" height="{h}" fill="{BLACK}"/>']
    b.append(text(60, 20, "RANK", GREY, px=2))
    b.append(text(150, 20, "NAME", GREY, px=2))
    b.append(text(260, 20, "CATEGORIA", GREY, px=2))
    b.append(text(W - 60 - text_width("SCORE", 2), 20, "SCORE", GREY, px=2))
    b.append(f'<rect x="60" y="44" width="{W - 120}" height="2" fill="{GREY_DK}"/>')
    for i, (rank, name, cat, score, col) in enumerate(rows):
        y = 60 + i * 34
        g = f'<g>{blink("1.4s", "1;1;0.25;1") if i == 0 else ""}'
        g += text(60, y, rank, col, px=2) + text(150, y, name, col, px=2) + text(260, y, cat, WHITE, px=2)
        g += text(W - 60 - text_width(f"{score:07d}", 2), y, f"{score:07d}", col, px=2) + "</g>"
        b.append(g)
    b.append(f'<rect x="60" y="{h - 48}" width="{W - 120}" height="2" fill="{GREY_DK}"/>')
    b.append(text(60, h - 34, f"PLACAR DO GITHUB EM {DATA} · INCLUI REPOS PRIVADOS", GREY_DK, px=2))
    save("m2-highscore.svg", svg(W, h, "".join(b) + scanlines(W, h, 0.14), title="High score: PRs, commits, fases, open source"))


# ========================================================= MODELO 3: CARTUCHO
PLASTIC, PLASTIC_DK, PLASTIC_LT = "#9AA3AD", "#6F7A85", "#C4CBD2"


def m3_cartucho():
    h = 330
    b = [f'<rect width="{W}" height="{h}" fill="{NAVY_DK}"/>']
    # padrão de fundo (pontinhos)
    b.append('<defs><pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse">'
             f'<rect x="7" y="7" width="2" height="2" fill="{GREY_DK}"/></pattern></defs>'
             f'<rect width="{W}" height="{h}" fill="url(#dots)"/>')
    # corpo do cartucho
    cx, cy, cw, chh = 100, 16, 680, 300
    b.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{chh}" fill="{PLASTIC}"/>')
    b.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="6" fill="{PLASTIC_LT}"/>')
    b.append(f'<rect x="{cx}" y="{cy}" width="6" height="{chh}" fill="{PLASTIC_LT}"/>')
    b.append(f'<rect x="{cx + cw - 6}" y="{cy}" width="6" height="{chh}" fill="{PLASTIC_DK}"/>')
    b.append(f'<rect x="{cx}" y="{cy + chh - 6}" width="{cw}" height="6" fill="{PLASTIC_DK}"/>')
    # ranhuras laterais (grip)
    for i in range(6):
        y = cy + 40 + i * 14
        b.append(f'<rect x="{cx + 16}" y="{y}" width="28" height="4" fill="{PLASTIC_DK}"/>')
        b.append(f'<rect x="{cx + cw - 44}" y="{y}" width="28" height="4" fill="{PLASTIC_DK}"/>')
    # entalhe inferior (conector)
    b.append(f'<rect x="{cx + 60}" y="{cy + chh - 28}" width="{cw - 120}" height="22" fill="{PLASTIC_DK}"/>')
    for i in range(0, cw - 140, 12):
        b.append(f'<rect x="{cx + 70 + i}" y="{cy + chh - 24}" width="6" height="14" fill="{YELLOW}" opacity="0.7"/>')
    # etiqueta
    lx, ly, lw, lh = cx + 60, cy + 28, cw - 120, 232
    b.append(f'<rect x="{lx}" y="{ly}" width="{lw}" height="{lh}" fill="{CREAM}"/>')
    b.append(f'<rect x="{lx}" y="{ly}" width="{lw}" height="44" fill="{PINK}"/>')
    b.append(f'<rect x="{lx}" y="{ly + 44}" width="{lw}" height="6" fill="{NAVY}"/>')
    b.append(text(lx + 20, ly + 10, "PAGALEVE", WHITE, px=2))
    b.append(text(lx + lw - 20 - text_width("16-BIT · PT-BR", 2), ly + 12, "16-BIT · PT-BR", WHITE, px=2))
    # arte: sprite em cena
    b.append(f'<rect x="{lx + 20}" y="{ly + 66}" width="150" height="130" fill="{NAVY}"/>')
    for i, yy in enumerate((ly + 150, ly + 164, ly + 180)):
        b.append(f'<rect x="{lx + 20}" y="{yy}" width="150" height="2" fill="{BLUE}" opacity="{0.4 + i * 0.2}"/>')
    b.append(icon("star", lx + 34, ly + 78, px=2))
    b.append(icon("star", lx + 140, ly + 90, px=2))
    b.append(icon("coin", lx + 128, ly + 128, px=3))
    b.append(sprite(lx + 60, ly + 84, CHARACTER, CHAR_PAL, px=5))
    b.append(f'<rect x="{lx + 20}" y="{ly + 194}" width="150" height="2" fill="{CYAN}"/>')
    # textos da etiqueta
    tx = lx + 196
    b.append(text(tx, ly + 70, NAME, NAVY, px=4))
    b.append(text(tx, ly + 118, CLASSE, PINK, px=3))
    b.append(text(tx, ly + 148, "INTEGRAÇÕES · AUTOMAÇÃO", GREY_DK, px=2))
    b.append(text(tx, ly + 166, "INCIDENTES · SUPORTE TÉCNICO", GREY_DK, px=2))
    b.append(text(tx, ly + 184, "FINTECH · PIX PARCELADO", GREY_DK, px=2))
    b.append(f'<rect x="{tx}" y="{ly + 204}" width="{lw - 216}" height="2" fill="{NAVY}"/>')
    b.append(text(tx, ly + 210, "PGLV-001", NAVY, px=2))
    b.append(text(tx + 120, ly + 210, "1 JOGADOR", NAVY, px=2))
    b.append(text(lx + lw - 20 - text_width(f"LV {SEMESTRE:02d}", 3), ly + 204, f"LV {SEMESTRE:02d}", PINK, px=3))
    save("m3-cartucho.svg", svg(W, h, "".join(b), title="Cartucho: Gabriel Jesus, Solutions Engineer"))


def m3_save():
    slots = [
        ("SLOT 1", "PAGALEVE", "SOLUTIONS ENGINEER PLENO", f"{PRS_MERGED} PRS · {COMMITS} COMMITS", 1.0, PINK),
        ("SLOT 2", "ENG. DA COMPUTAÇÃO", f"{SEMESTRE}º SEMESTRE", f"{SEMESTRE * 10}% CONCLUÍDO", SEMESTRE / 10, YELLOW),
        ("SLOT 3", "OPEN SOURCE", "ACTIVEMERCHANT/PAYMENT_ICONS", "ÍCONE PAGALEVE · MERGED", 1.0, LIME),
    ]
    sh, gap = 76, 10
    h = 56 + len(slots) * (sh + gap)
    b = [f'<rect width="{W}" height="{h}" fill="{CREAM}"/>',
         f'<rect x="0" y="0" width="{W}" height="4" fill="{NAVY}"/>',
         f'<rect x="0" y="{h - 4}" width="{W}" height="4" fill="{NAVY}"/>',
         text(24, 14, "SAVE DATA", NAVY, px=3),
         text(W - 24 - text_width(f"ÚLTIMO SAVE {DATA}", 2), 18, f"ÚLTIMO SAVE {DATA}", GREY_DK, px=2)]
    for i, (slot, t1, t2, t3, pct, col) in enumerate(slots):
        y = 50 + i * (sh + gap)
        b.append(f'<rect x="24" y="{y}" width="{W - 48}" height="{sh}" fill="{NAVY}"/>')
        b.append(f'<rect x="28" y="{y + 4}" width="{W - 56}" height="{sh - 8}" fill="{NAVY_DK}"/>')
        b.append(icon("floppy", 44, y + 22, px=4))
        b.append(text(96, y + 14, slot, col, px=2))
        b.append(text(96, y + 42, t1, WHITE, px=2))
        b.append(text(320, y + 14, t2, GREY, px=2))
        b.append(text(320, y + 42, t3, WHITE, px=2))
        b.append(bar(W - 212, y + 26, 164, 20, pct, fg=col, px=4, segments=8))
    save("m3-save.svg", svg(W, h, "".join(b), title="Save data"))


def m3_controles():
    h = 150
    b = [f'<rect width="{W}" height="{h}" fill="{CREAM}"/>',
         f'<rect x="0" y="0" width="{W}" height="4" fill="{NAVY}"/>',
         f'<rect x="0" y="{h - 4}" width="{W}" height="4" fill="{NAVY}"/>',
         text(24, 14, "CONTROLES", NAVY, px=3)]
    # d-pad
    dp = ["...nnn....", "...nwn....", "nnnnwnnnn.", "nwwwwwwwn.", "nnnnwnnnn.", "...nwn....", "...nnn...."]
    b.append(sprite(40, 52, dp, {"n": NAVY, "w": GREY}, px=8))
    btns = [("A", PINK, "ABRIR CHAMADO → RESOLVER"), ("B", BLUE, "INTEGRAR LOJA → VTEX, SHOPIFY, NUVEMSHOP..."),
            ("X", LIME, "AUTOMATIZAR → N8N, LAMBDA"), ("Y", YELLOW, "CONSULTAR → SNOWFLAKE, METABASE")]
    for i, (letter, col, desc) in enumerate(btns):
        y = 50 + i * 24
        b.append(f'<rect x="150" y="{y}" width="20" height="20" fill="{col}"/>')
        b.append(f'<rect x="150" y="{y + 16}" width="20" height="4" fill="{BLACK}" opacity="0.3"/>')
        b.append(text(156, y + 2, letter, WHITE if letter != "Y" else NAVY, px=2))
        b.append(text(184, y + 2, desc, NAVY, px=2))
    save("m3-controles.svg", svg(W, h, "".join(b), title="Controles"))


if __name__ == "__main__":
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    if only in (None, "m1"):
        m1_header(); m1_atributos(); m1_party()
        inventory("m1-inventario.svg", "INVENTÁRIO", NAVY_DK, WHITE, GREY_DK, NAVY, WHITE, GREY, PINK)
        for key, title in (("quests", "QUEST LOG"), ("inventario", "INVENTÁRIO"), ("party", "PARTY"), ("contato", "TAVERNA (CONTATO)"), ("stats", "SAVE FILE")):
            section_banner(f"m1-sec-{key}.svg", title, "rpg")
    if only in (None, "m2"):
        m2_hud(); m2_stages(); m2_continue(); m2_highscore()
        inventory("m2-powerups.svg", "POWER-UPS", BLACK, CYAN, PINK_DK, NAVY_DK, WHITE, CYAN, PINK)
        for key, title in (("player", "PLAYER SELECT"), ("stages", "STAGE SELECT"), ("highscore", "HIGH SCORE")):
            section_banner(f"m2-sec-{key}.svg", title, "arcade")
    if only in (None, "m3"):
        m3_cartucho(); m3_save(); m3_controles()
        inventory("m3-itens.svg", "ITENS", CREAM, NAVY, GREY, NAVY, WHITE, CYAN, NAVY)
        for key, title in (("historia", "HISTÓRIA"), ("fases", "FASES"), ("itens", "ITENS"), ("save", "SAVE DATA"), ("suporte", "SUPORTE TÉCNICO")):
            section_banner(f"m3-sec-{key}.svg", title, "manual")
