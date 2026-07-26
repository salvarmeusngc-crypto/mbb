import subprocess, os
os.chdir(r"c:\Users\mattq\Downloads\hl do cara\mbb")
subprocess.run(["git","config","core.longpaths","true"], capture_output=True)
for c in [
    ["git","add","-A"],
    ["git","commit","-m","3messes: site kuromi completo - video texto cartinha timer"],
    ["git","pull","--rebase","--autostash"],
    ["git","push"]
]:
    r = subprocess.run(c, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(" ".join(c), "→", r.returncode)
    if r.stdout.strip(): print(r.stdout.strip()[:200])
    if r.returncode != 0 and r.stderr.strip(): print("ERR:", r.stderr.strip()[:200])
print("DONE")
