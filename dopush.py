import subprocess, os, glob

os.chdir(r"c:\Users\mattq\Downloads\hl do cara\mbb")

# Habilita suporte a nomes longos no git (fix Windows)
subprocess.run(["git","config","core.longpaths","true"], capture_output=True)

# Adiciona tudo exceto a pasta 3messes por enquanto (tem arquivo com nome longo)
# Primeiro tenta add tudo
r = subprocess.run(["git","add","-A"], capture_output=True, text=True, encoding="utf-8", errors="replace")
print("git add -A:", r.returncode)
if r.returncode != 0:
    print("STDERR:", r.stderr[:300])
    # Fallback: adiciona arquivo a arquivo ignorando erros
    subprocess.run(["git","add","index.html","2messes/","1mes/","valentines/",
                    "cinnamoroll/","src/","pfp/","fotos nossas/","pngwing.com.png",
                    "pngwing.com (1).png","pngwing.com (2).png"], 
                   capture_output=True)
    print("Fallback add done")

# Commit
r2 = subprocess.run(["git","commit","-m",
    "fix: listra central removida; musica autoplay 2messes; fotos retrato; yt api"],
    capture_output=True, text=True, encoding="utf-8", errors="replace")
print("commit:", r2.stdout.strip() or r2.stderr.strip())

# Pull + push
r3 = subprocess.run(["git","pull","--rebase","--autostash"],
    capture_output=True, text=True, encoding="utf-8", errors="replace")
print("pull:", r3.stdout.strip()[:200], r3.stderr.strip()[:200])

r4 = subprocess.run(["git","push"],
    capture_output=True, text=True, encoding="utf-8", errors="replace")
print("push:", r4.stdout.strip(), r4.stderr.strip()[:300])

print("DONE")
