import re

filepath = r"c:\Users\mattq\Downloads\hl do cara\mbb\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the versions-grid div start
grid_start = content.find('<div class="versions-grid">')

# Find the closing div of the wrapper that contains card-2meses
card2_pos = content.find('card-2meses')
# Find the </a> that closes the card-2meses anchor
a_close = content.find('</a>', card2_pos)
# Find the </div> that closes the wrapper
div_close = content.find('</div>', a_close)

print(f"grid_start: {grid_start}")
print(f"card2_pos: {card2_pos}")
print(f"a_close: {a_close}")
print(f"div_close: {div_close}")

if grid_start == -1:
    print("ERROR: versions-grid not found!")
    exit(1)

before = content[:grid_start]
after = content[div_close + 6:]  # +6 for len("</div>")

new_grid = '''    <div class="versions-grid">

        <!-- CARD 1 MES -->
        <a class="version-card card-1mes" href="#" data-dest="1mes/index.html" data-load="load1mes">
            <span class="badge">\u2713 ao vivo</span>
            <img src="src/73b0ea4d4bb31426c173754d20228246.gif" class="card-gif" alt="pompompurin">
            <h2>1 m\u00eas de namoro</h2>
            <div class="divider"></div>
            <p>o come\u00e7o de tudo, o primeiro m\u00eas com voc\u00ea do meu lado \u2661</p>
            <button class="card-btn">ver agora</button>
        </a>

        <!-- CARD DIA DOS NAMORADOS -->
        <a class="version-card card-valentines" href="#" data-dest="valentines/index.html" data-load="loadValentines">
            <span class="badge">\U0001f499 novo</span>
            <img src="cinnamoroll/62479586fa237d932487c8684b776161.gif" class="card-gif" alt="cinnamoroll">
            <h2>dia dos namorados</h2>
            <div class="divider"></div>
            <p>especial cinnamoroll \u2014 feito com todo amor pra voc\u00ea \U0001f499</p>
            <button class="card-btn">ver agora</button>
        </a>

        <!-- CARD 2 MESES -->
        <a class="version-card card-2meses" href="#" data-dest="2messes/index.html" data-load="load2meses">
            <span class="badge">novo</span>
            <img src="2messes/sanrio STICKER.gif" class="card-gif" alt="my melody" onerror="this.style.display=\'none\'">
            <h2>2 meses de namoro</h2>
            <div class="divider"></div>
            <p>nosso cantinho \u2014 especial my melody pra voc\u00ea \u2661</p>
            <button class="card-btn">entrar no cantinho</button>
        </a>

    </div>'''

result = before + new_grid + after

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print("Done! File updated successfully.")
print(f"Total length: {len(result)}")
