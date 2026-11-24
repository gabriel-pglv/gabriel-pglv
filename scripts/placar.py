"""Busca os números do placar na API do GitHub e imprime no formato KEY=VALUE.

Uso: GITHUB_TOKEN=... python3 -I scripts/placar.py >> "$GITHUB_ENV"
Conta PRs mergeadas e commits de autoria do usuário pela search API; com um
token pessoal do próprio usuário, a contagem inclui repositórios privados.
"""
import json, os, sys, urllib.request, urllib.parse, datetime

USER = os.environ.get("PROFILE_USER", "gabriel-pglv")
TOKEN = os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    sys.exit("GITHUB_TOKEN ausente")


def search(kind, query, accept="application/vnd.github+json"):
    url = f"https://api.github.com/search/{kind}?per_page=1&q=" + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}", "Accept": accept,
                                               "User-Agent": "placar-readme"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["total_count"]


prs = search("issues", f"author:{USER} type:pr is:merged")
commits = search("commits", f"author:{USER}", "application/vnd.github.cloak-preview+json")
today = datetime.date.today().strftime("%d.%m.%Y")
print(f"PRS_MERGED={prs}\nCOMMITS={commits}\nDATA={today}")
