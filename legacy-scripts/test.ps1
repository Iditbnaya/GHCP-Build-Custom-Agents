# script to check if spooler service is running and start it if not
$serviceName = "Spooler"
$service = Get-Service -Name $serviceName -ErrorAction SilentlyContinue
if ($service -eq $null) {
    Write-Host "Service $serviceName not found."
} elseif ($service.Status -ne 'Running') {
    Write-Host "Service $serviceName is not running. Starting service..."
    Start-Service -Name $serviceName
    Write-Host "Service $serviceName started."
} else {
    Write-Host "Service $serviceName is already running."
}

