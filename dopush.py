import subprocess, os
os.chdir(r"c:\Users\mattq\Downloads\hl do cara\mbb")
cmds = [
    ["git","add","-A"],
    ["git","commit","-m","fix: remove listra central; musica autoplay; fotos no retrato; alteracoes 2messes"],
    ["git","pull","--rebase"],
    ["git","push"]
]
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(" ".join(c))
    print(r.stdout.strip())
    if r.returncode != 0 and r.stderr.strip():
        print("STDERR:", r.stderr.strip())
print("DONE")
