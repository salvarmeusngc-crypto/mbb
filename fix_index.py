import re

path = r"c:\Users\mattq\Downloads\hl do cara\mbb\index.html"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove o div separado do card 2meses que ficou fora do versions-grid
# e move o card pra dentro do grid

old = '''    </div>
    <!-- CARD 2 MESES - centralizado abaixo -->
    <div style="display:flex;justify-content:center;margin-top:0;">
        <a class="version-card card-2meses" href="#" data-dest="2messes/index.html" data-load="load2meses">
            <span class="badge">novo</span>
            <img src="2messes/sanrio STICKER.gif" class="card-gif" alt="my melody" onerror="this.style.display='none'">
            <h2>2 meses de namoro</h2>
            <div class="divider"></div>
            <p>nosso cantinho - especial my melody pra voce</p>
            <button class="card-btn">entrar no cantinho</button>
        </a>
    </div>'''

new = '''        <!-- CARD 2 MESES -->
        <a class="version-card card-2meses" href="#" data-dest="2messes/index.html" data-load="load2meses">
            <span class="badge">novo</span>
            <img src="2messes/sanrio STICKER.gif" class="card-gif" alt="my melody" onerror="this.style.display=\'none\'">
            <h2>2 meses de namoro</h2>
            <div class="divider"></div>
            <p>nosso cantinho - especial my melody</p>
            <button class="card-btn">entrar no cantinho</button>
        </a>

    </div>'''

if old in content:
    content = content.replace(old, new)
    print("OK: substituicao feita")
else:
    print("ERRO: texto nao encontrado")
    # debug: mostra os primeiros chars ao redor de versions-grid
    idx = content.find('versions-grid')
    print(f"versions-grid found at: {idx}")
    idx2 = content.find('CARD 2 MESES')
    print(f"CARD 2 MESES found at: {idx2}")
    if idx2 > 0:
        print(repr(content[idx2-200:idx2+300]))

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
