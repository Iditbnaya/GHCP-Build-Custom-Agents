.

$firstName = "Dana"
$lastName = "Cohen"
$department = "Claims"
$manager = "Avi Levi"
$password = "Welcome123"
$domainController = "DC01.corp.local"
$ou = "OU=Users,OU=Healthcare,DC=corp,DC=local"
$homeDriveRoot = "\\FILE01\HomeFolders"
$logFile = "C:\Temp\employee_setup.log"

$userName = ($firstName.Substring(0, 1) + $lastName).ToLower()
$displayName = $firstName + " " + $lastName
$email = $userName + "@corp.local"

Write-Host "Creating user $displayName"
Add-Content $logFile "Starting setup for $displayName at $(Get-Date)"

New-ADUser -Name $displayName -GivenName $firstName -Surname $lastName -SamAccountName $userName -UserPrincipalName $email -Department $department -Manager $manager -Path $ou -AccountPassword (ConvertTo-SecureString $password -AsPlainText -Force) -Enabled $true -Server $domainController

Add-ADGroupMember -Identity "All Employees" -Members $userName -Server $domainController
Add-ADGroupMember -Identity "Claims Users" -Members $userName -Server $domainController
Add-ADGroupMember -Identity "VPN Users" -Members $userName -Server $domainController

$homeFolder = $homeDriveRoot + "\" + $userName
New-Item -ItemType Directory -Path $homeFolder

$acl = Get-Acl $homeFolder
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("corp\$userName", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$acl.SetAccessRule($rule)
Set-Acl $homeFolder $acl

Set-ADUser -Identity $userName -HomeDirectory $homeFolder -HomeDrive "H:" -Server $domainController

Add-Content $logFile "Finished setup for $displayName with password $password"
Write-Host "User created and added to groups"