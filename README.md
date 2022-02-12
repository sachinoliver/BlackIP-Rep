# BlackIP-Rep
BlackIP-Rep is a tool designed to gather the reputation and information of Blacklisted IP's. The tool will collect evidence from major spamlists. The tool is mainly is focused on incresing the workflow of Security Operations(SOC) team during investigation. 

# Functionality
BlackIP-Rep accepts Bulk list of IP address which you need to check whether they are blacklisted or not, then BlackIP-Rep will check the list of IPs with Bulkblacklist.com and collect all the poor reputed IP or the Blacklisted ones and save that page as pdf for evidence. For further investion proofs the tool will check the repution and take screenshot from mxtoolbox or from virustotal  for more evidence. The tool will also collect information such as the location, ASN, Service Provider of the list of IP provided.



# requirements
```
pip install -r requirements.txt
```


## Services used:
* Mxtoolbox
* Bulkblacklist
  * Spamcorp,
  * Spamhaus,
  * Barracuda.
* Virustotal
* Infobyip




# Contributors
