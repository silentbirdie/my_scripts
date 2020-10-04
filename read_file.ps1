#what is the file?
$n=Read-Host ("enter a filepath")

#test the file

test-path -path "$n"

#show contents of file

if ($?) 
{ more "$n" }

#say it doesn't exist

ifelse 
{echo "file doesn't exist"}
