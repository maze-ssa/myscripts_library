#Copy & Install Software from a mapped network Drive
$softwareName = "example.exe"
$networkPath = "\\server\share\$softwareName"
$destination = "D:\Software\"

# Create the destination folder if it does not exist
if (!(Test-Path $destination)) {
    New-Item -ItemType Directory -Path $destination
}

# Check if the software is already installed
if (!(Get-ItemProperty -Path HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName | Where-Object {$_.DisplayName -eq $softwareName})) {
    # Copy the software from the network drive to the destination folder
    Copy-Item -Path $networkPath -Destination $destination

    # Install the software
    Start-Process -FilePath "$destination\$softwareName" -ArgumentList '/S' -Wait
}
else {
    Write-Host "$softwareName is already installed."
}
