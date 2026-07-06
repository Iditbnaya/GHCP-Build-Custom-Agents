

$servers = "FILE01", "APP01", "DB01"
$smtpServer = "smtp.corp.local"
$to = "it-ops@corp.local"
$from = "server-monitor@corp.local"
$subject = "Disk space report"
$reportFile = "C:\Temp\disk_report.txt"

"Disk report created at $(Get-Date)" | Out-File $reportFile
"==================================" | Out-File $reportFile -Append

foreach ($server in $servers) {
    Write-Host "Checking $server"

    $disks = Get-WmiObject Win32_LogicalDisk -ComputerName $server -Filter "DriveType=3"

    foreach ($disk in $disks) {
        $freeGb = [math]::Round($disk.FreeSpace / 1GB, 2)
        $totalGb = [math]::Round($disk.Size / 1GB, 2)
        $line = $server + " " + $disk.DeviceID + " free: " + $freeGb + "GB of " + $totalGb + "GB"

        Write-Host $line
        Add-Content $reportFile $line

        if ($freeGb -lt 10) {
            Add-Content $reportFile "WARNING: low disk space on $server $($disk.DeviceID)"
        }
    }
}

$body = Get-Content $reportFile | Out-String
Send-MailMessage -SmtpServer $smtpServer -To $to -From $from -Subject $subject -Body $body

Write-Host "Report sent"