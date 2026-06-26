$file = "c:\Users\mattq\Downloads\hl do cara\mbb\index.html"
$content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)

# Find the versions-grid start
$gridStart = $content.IndexOf('<div class="versions-grid">')
# Find the separate wrapper div that contains the card-2meses
$wrapperEnd = $content.IndexOf('</div>', $content.IndexOf('card-2meses')) + 6

if ($gridStart -eq -1) {
    Write-Host "ERROR: versions-grid not found"
    exit 1
}

Write-Host "gridStart: $gridStart"
Write-Host "wrapperEnd: $wrapperEnd"

$before = $content.Substring(0, $gridStart)
$after = $content.Substring($wrapperEnd)

$newGrid = @"
    <div class="versions-grid">

        <!-- CARD 1 MES -->
        <a class="version-card card-1mes" href="#" data-dest="1mes/index.html" data-load="load1mes">
            <span class="badge">ao vivo</span>
            <img src="src/73b0ea4d4bb31426c173754d20228246.gif" class="card-gif" alt="pompompurin">
            <h2>1 mes de namoro</h2>
            <div class="divider"></div>
            <p>o comeco de tudo, o primeiro mes com voce do meu lado</p>
            <button class="card-btn">ver agora</button>
        </a>

        <!-- CARD DIA DOS NAMORADOS -->
        <a class="version-card card-valentines" href="#" data-dest="valentines/index.html" data-load="loadValentines">
            <span class="badge">novo</span>
            <img src="cinnamoroll/62479586fa237d932487c8684b776161.gif" class="card-gif" alt="cinnamoroll">
            <h2>dia dos namorados</h2>
            <div class="divider"></div>
            <p>especial cinnamoroll feito com todo amor pra voce</p>
            <button class="card-btn">ver agora</button>
        </a>

        <!-- CARD 2 MESES -->
        <a class="version-card card-2meses" href="#" data-dest="2messes/index.html" data-load="load2meses">
            <span class="badge">novo</span>
            <img src="2messes/sanrio STICKER.gif" class="card-gif" alt="my melody" onerror="this.style.display='none'">
            <h2>2 meses de namoro</h2>
            <div class="divider"></div>
            <p>nosso cantinho especial my melody pra voce</p>
            <button class="card-btn">entrar no cantinho</button>
        </a>

    </div>
"@

$result = $before + $newGrid + $after
[System.IO.File]::WriteAllText($file, $result, [System.Text.Encoding]::UTF8)
Write-Host "Done! File updated."
