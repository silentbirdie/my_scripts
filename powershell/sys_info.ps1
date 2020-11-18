$choix="o"
while( $choix -eq "o")
{
    Write-Output "1 - nom de bios"
    Write-Output "2 - liste de diskes"
    Write-Output "3 - version du systeme d'operation"
    Write-Output "Q - quitter"
    $choix=Read-Host("votre choix")
    switch ($choix)
    {
        1 { 
            Get-WmiObject Win32_bios | Select-Object name ; break
        }
        2 { 
            $disk_properties=Get-WmiObject  win32_logicaldisk
            Write-Output $disk_properties | Select-Object -property deviceid, volumename,
            @{L='FreeSpaceGB';E={"{0:N2}" -f ($_.FreeSpace /1GB)}},
            @{L="Capacity";E={"{0:N2}" -f ($_.Size/1GB)}} ; break 
        }
        3 { 
            Get-WmiObject win32_operatingsystem | Select-Object version 
        }
        [Qq] { 
            break 
        }
        default { " $_ : Mauvais choix..." }
        }
}