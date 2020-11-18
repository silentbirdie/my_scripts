#
# Windows PowerShell script for AD DS Deployment
# Admin password will be the same as local administrator
# Change the Domain name to whatever you want before executing script
#
$DomainName = Read-Host "what will be the domain name?"
$DomainNetBiosName = Read-Host "what will be the netbios name"
$AD_Database_Path = Read-Host "what will be the databasepath, sysvolpath and logpath?
default is normally C:"
Import-Module ServerManager

Install-WindowsFeature AD-Domain-Services -IncludeAllSubFeature -IncludeManagementTools
Install-WindowsFeature DNS -IncludeAllSubFeature -IncludeManagementTools

Import-Module ADDSDeployment
Import-Module DnsServer

Install-ADDSForest `
 -DomainName $DomainName `
 -DomainNetbiosName $DomainNetBiosName -DomainMode Win2012R2 -ForestMode Win2012R2 -DatabasePath $AD_Database_Path\Windows\NTDS -SysvolPath $AD_Database_Path\Windows\SYSVOL -LogPath $AD_Database_Path\Windows\Logs -Force
