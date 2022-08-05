#Script to obfuscate other scripts using Invoke-Obfuscation
Import-Module /home/kali/Master_Thesis/Invoke-Obfuscation/Invoke-Obfuscation.psd1
$stopwatch =  [system.diagnostics.stopwatch]::StartNew()

#Picks a random powershell script from the numbered scripts.
#Checks if the script already exists in out directory
#Checks if the file exists in in directory
#Then obfuscates it with the assigned method.

function obfuscate($command,$outPath){
    write-host ("Starting for $outPath") -ForegroundColor green
	for ($i = 1 ; $i -le 10000 ; $i++){
		if($i % 1000 -eq 0){
			write-host ("Elapsed time for " + $i + " obfuscations are: ")
			$stopwatch
		}
		$inCounter = Get-Random -Maximum 399894
		$commentRemover = 'Token,Comment,1,home,'
		$inFile = "/home/kali/Master_Thesis/Powershell_Scripts_Renamed/" + $inCounter + ".ps1"
		$finalCommand = $commentRemover + $command
		$outFile = $outPath + $inCounter + ".ps1"
		
		#For base64
		#$outFile = $outPath + $inCounter + ".b64"

		$plainControlFile = "/home/kali/Master_Thesis/Plain_control/Plain/" + $inCounter + ".ps1"

		#i++ and i-- in order to add the correct number of files
		Try {
			if( -not [System.IO.File]::Exists($outFile)){
				if([System.IO.File]::Exists($inFile)){
					write-host $inCounter
					#This is the one we use for all the obfuscations except base64
					Invoke-Obfuscation -ScriptPath $inFile -Command $finalCommand -Quiet  > $outFile

					#Check that it is actually obfuscating
					if([System.IO.File]::Exists($plainControlFile)){
						if ((Get-FileHash $plainControlFile).Hash -eq (Get-FileHash $outFile).Hash){
							write-host("removed Since same")
							write-host ($outFile)
							Remove-Item $outFile
							$i--
						}
					} else {
						Invoke-Obfuscation -ScriptPath $inFile -Command $commentRemover -Quiet  > $plainControlFile
						if ((Get-FileHash $plainControlFile).Hash -eq (Get-FileHash $outFile).Hash){
							write-host("removed since same")
							write-host ($outFile)
							Remove-Item $outFile
							$i--
						}
					}

					$i++

					#This for base64
					$content = get-content $inFile
					#echo ([Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($content))) > $outFile

				}
			}
		}
		Catch {
			Remove-Item $outFile
		}
		$i--
	}
}
