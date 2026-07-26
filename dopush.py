import subprocess, os

os.chdir(r"c:\Users\mattq\Downloads\hl do cara\mbb")
subprocess.run(["git","config","core.longpaths","true"], capture_output=True)

cmds = [
    ["git","add","-A"],
    ["git","commit","-m","3meses: experiencia premium kuromi/loli baloes; index: 4 cards; listra removida"],
    ["git","pull","--rebase","--autostash"],
    ["git","push"]
]
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(" ".join(c))
    print(r.stdout.strip()[:300])
    if r.returncode != 0 and r.stderr.strip():
        print("STDERR:", r.stderr.strip()[:300])
print("DONE")
