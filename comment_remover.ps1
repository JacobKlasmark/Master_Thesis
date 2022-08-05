Import-Module /home/kali/Master_Thesis/Invoke-Obfuscation/Invoke-Obfuscation.psd1
$stopwatch =  [system.diagnostics.stopwatch]::StartNew()

$source_files_dir = "/home/kali/Master_Thesis/source_files/"
$dest_files_dir = "/home/kali/Master_Thesis/dest_files/"
$counter = 0

foreach ($file in Get-ChildItem $source_files_dir){
  $file = (Get-Item $file).Name
  $commentRemover = 'Token,Comment,1,home,'
  $inFile = $source_files_dir + $file
  $outFile = $dest_files_dir + $counter + ".ps1"

  Invoke-Obfuscation -ScriptPath $inFile -Command $commentRemover -Quiet  > $outFile
  $counter = $counter + 1

}

Remove-Module Invoke-Obfuscation

write-host ("Number of files cleaned: " + $counter)
write-host ("Elapsed Time since we started obfuscation: ")
$stopwatch
