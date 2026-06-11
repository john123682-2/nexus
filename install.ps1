Write-Host "Installing NEXUS..."

$folder = "$env:USERPROFILE\nexus"

if (!(Test-Path $folder)) {
    New-Item -ItemType Directory -Force -Path $folder
}

git clone https://github.com/john123682-2/nexus.git $folder

Write-Host ""
Write-Host "NEXUS Installed!"
Write-Host "Location: $folder"