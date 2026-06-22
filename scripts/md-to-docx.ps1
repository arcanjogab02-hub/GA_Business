<#
  md-to-docx.ps1 — Conversor minimalista de Markdown simples para .docx (OOXML puro, sem dependências).
  Uso:
    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\md-to-docx.ps1 -In entrada.md -Out saida.docx

  Marcadores suportados (um por linha):
    # Titulo          -> título grande (preto, bold)
    ## Secao          -> seção (dourado, bold)
    ### Rotulo        -> rótulo pequeno (dourado, bold)
    - item            -> bullet
    > nota            -> nota (cinza, itálico)
    ---               -> linha divisória
    [__]              -> linha em branco pra resposta
    (linha vazia)     -> espaçamento
    qualquer texto    -> parágrafo normal
  Inline: **negrito**.
#>
param(
  [Parameter(Mandatory=$true)][string]$In,
  [Parameter(Mandatory=$true)][string]$Out
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression | Out-Null

$gold = 'B58A00'
$dark = '1A1A1A'
$gray = '808080'

function Esc([string]$s){
  $s = $s -replace '&','&amp;'
  $s = $s -replace '<','&lt;'
  $s = $s -replace '>','&gt;'
  return $s
}

function Runs([string]$text, [string]$rprBase){
  $out = ''
  $parts = [regex]::Split($text, '(\*\*.*?\*\*)')
  foreach($p in $parts){
    if($p -eq ''){ continue }
    if($p -match '^\*\*(.*)\*\*$'){
      $t = Esc $matches[1]
      $out += "<w:r><w:rPr>$rprBase<w:b/></w:rPr><w:t xml:space='preserve'>$t</w:t></w:r>"
    } else {
      $t = Esc $p
      $out += "<w:r><w:rPr>$rprBase</w:rPr><w:t xml:space='preserve'>$t</w:t></w:r>"
    }
  }
  if($out -eq ''){ $out = "<w:r><w:rPr>$rprBase</w:rPr><w:t xml:space='preserve'></w:t></w:r>" }
  return $out
}

$lines = Get-Content -LiteralPath $In -Encoding UTF8
$body = ''

foreach($raw in $lines){
  $line = $raw.TrimEnd()
  if($line -eq ''){
    $body += "<w:p><w:pPr><w:spacing w:after='60'/></w:pPr></w:p>"
    continue
  }
  if($line -eq '---'){
    $body += "<w:p><w:pPr><w:pBdr><w:bottom w:val='single' w:sz='6' w:space='1' w:color='D9D9D9'/></w:pBdr><w:spacing w:before='80' w:after='160'/></w:pPr></w:p>"
    continue
  }
  if($line -eq '[__]'){
    $body += "<w:p><w:pPr><w:pBdr><w:bottom w:val='single' w:sz='4' w:space='6' w:color='BFBFBF'/></w:pBdr><w:spacing w:before='40' w:after='200'/></w:pPr></w:p>"
    continue
  }
  if($line.StartsWith('### ')){
    $r = Runs $line.Substring(4) "<w:b/><w:color w:val='$gold'/><w:sz w:val='18'/>"
    $body += "<w:p><w:pPr><w:spacing w:before='120' w:after='40'/></w:pPr>$r</w:p>"
    continue
  }
  if($line.StartsWith('## ')){
    $r = Runs $line.Substring(3) "<w:b/><w:color w:val='$gold'/><w:sz w:val='26'/>"
    $body += "<w:p><w:pPr><w:spacing w:before='240' w:after='80'/></w:pPr>$r</w:p>"
    continue
  }
  if($line.StartsWith('# ')){
    $r = Runs $line.Substring(2) "<w:b/><w:color w:val='$dark'/><w:sz w:val='40'/>"
    $body += "<w:p><w:pPr><w:spacing w:after='40'/></w:pPr>$r</w:p>"
    continue
  }
  if($line.StartsWith('- ')){
    $r = Runs $line.Substring(2) "<w:color w:val='$dark'/><w:sz w:val='22'/>"
    $bullet = "<w:r><w:rPr><w:color w:val='$gold'/><w:sz w:val='22'/></w:rPr><w:t xml:space='preserve'>" + [char]0x2022 + "   </w:t></w:r>"
    $body += "<w:p><w:pPr><w:ind w:left='360' w:hanging='360'/><w:spacing w:after='60'/></w:pPr>$bullet$r</w:p>"
    continue
  }
  if($line.StartsWith('> ')){
    $r = Runs $line.Substring(2) "<w:i/><w:color w:val='$gray'/><w:sz w:val='20'/>"
    $body += "<w:p><w:pPr><w:spacing w:before='40' w:after='60'/></w:pPr>$r</w:p>"
    continue
  }
  $r = Runs $line "<w:color w:val='$dark'/><w:sz w:val='22'/>"
  $body += "<w:p><w:pPr><w:spacing w:after='80'/></w:pPr>$r</w:p>"
}

$sect = "<w:sectPr><w:pgSz w:w='11906' w:h='16838'/><w:pgMar w:top='1134' w:right='1134' w:bottom='1134' w:left='1134' w:header='708' w:footer='708' w:gutter='0'/></w:sectPr>"

$documentXml = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?><w:document xmlns:w='http://schemas.openxmlformats.org/wordprocessingml/2006/main'><w:body>$body$sect</w:body></w:document>"
$contentTypes = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?><Types xmlns='http://schemas.openxmlformats.org/package/2006/content-types'><Default Extension='rels' ContentType='application/vnd.openxmlformats-package.relationships+xml'/><Default Extension='xml' ContentType='application/xml'/><Override PartName='/word/document.xml' ContentType='application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml'/><Override PartName='/word/styles.xml' ContentType='application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml'/></Types>"
$rels = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?><Relationships xmlns='http://schemas.openxmlformats.org/package/2006/relationships'><Relationship Id='rId1' Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument' Target='word/document.xml'/></Relationships>"
$docRels = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?><Relationships xmlns='http://schemas.openxmlformats.org/package/2006/relationships'><Relationship Id='rId1' Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles' Target='styles.xml'/></Relationships>"
$styles = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?><w:styles xmlns:w='http://schemas.openxmlformats.org/wordprocessingml/2006/main'><w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii='Calibri' w:hAnsi='Calibri' w:cs='Calibri'/><w:sz w:val='22'/><w:szCs w:val='22'/></w:rPr></w:rPrDefault></w:docDefaults><w:style w:type='paragraph' w:default='1' w:styleId='Normal'><w:name w:val='Normal'/></w:style></w:styles>"

# valida o XML do documento antes de empacotar
$null = [xml]$documentXml

# garante a pasta de saída
$outDir = Split-Path -Parent $Out
if($outDir -and -not (Test-Path -LiteralPath $outDir)){ New-Item -ItemType Directory -Path $outDir -Force | Out-Null }
if(Test-Path -LiteralPath $Out){ Remove-Item -LiteralPath $Out -Force }

$enc = New-Object System.Text.UTF8Encoding($false)
$fs = [System.IO.File]::Open($Out, [System.IO.FileMode]::Create)
$zip = New-Object System.IO.Compression.ZipArchive($fs, [System.IO.Compression.ZipArchiveMode]::Create)
function Add-Entry($zip,$name,$content,$enc){
  $entry = $zip.CreateEntry($name)
  $s = $entry.Open()
  $bytes = $enc.GetBytes($content)
  $s.Write($bytes,0,$bytes.Length)
  $s.Dispose()
}
Add-Entry $zip '[Content_Types].xml' $contentTypes $enc
Add-Entry $zip '_rels/.rels' $rels $enc
Add-Entry $zip 'word/document.xml' $documentXml $enc
Add-Entry $zip 'word/styles.xml' $styles $enc
Add-Entry $zip 'word/_rels/document.xml.rels' $docRels $enc
$zip.Dispose()
$fs.Close()

Write-Output "OK -> $Out"
