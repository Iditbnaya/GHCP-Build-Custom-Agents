# user_export.ps1
# Legacy user-export automation (WORKSHOP SAMPLE - intentionally fragile).
# Goal for the demo: let the "Legacy Script Refactorer" agent find and fix the problems.
#
# Known problems to discover during the demo:
#   1. Hard-coded server and output path (no configuration).
#   2. No parameters - the script cannot be reused for another domain/OU/file.
#   3. CSV is built with string concatenation (breaks on commas, quotes, nulls).
#   4. No error handling and no logging.
#   5. Loads ALL users, then filters in a loop (inefficient and slow at scale).

$server  = "DC01.corp.local"
$outfile = "C:\exports\users.csv"

# Pulls every user in the directory, then filters later - wasteful.
$users = Get-ADUser -Filter * -Server $server -Properties Department, EmailAddress, Enabled

$csv = "Name,Email,Department,Enabled`n"
foreach ($u in $users) {
    if ($u.Department -eq "Infrastructure") {
        $csv = $csv + $u.Name + "," + $u.EmailAddress + "," + $u.Department + "," + $u.Enabled + "`n"
    }
}

Set-Content -Path $outfile -Value $csv
Write-Host "Done"
