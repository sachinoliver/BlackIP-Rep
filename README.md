# BlackIP-Rep
BlackIP-Rep is a tool designed to gather the reputation and information of Blacklisted IP's. The tool will collect evidence from major spamlists. The tool is mainly is focused on increasing the workflow of Security Operations(SOC) team during investigation. 


```

888888b.   888                   888      8888888 8888888b.         8888888b.                    
888  "88b  888                   888        888   888   Y88b        888   Y88b                   
888  .88P  888                   888        888   888    888        888    888                   
8888888K.  888  8888b.   .d8888b 888  888   888   888   d88P        888   d88P  .d88b.  88888b.  
888  "Y88b 888     "88b d88P"    888 .88P   888   8888888P"         8888888P"  d8P  Y8b 888 "88b 
888    888 888 .d888888 888      888888K    888   888        888888 888 T88b   88888888 888  888 
888   d88P 888 888  888 Y88b.    888 "88b   888   888               888  T88b  Y8b.     888 d88P 
8888888P"  888 "Y888888  "Y8888P 888  888 8888888 888               888   T88b  "Y8888  88888P"  
                                                                                        888      
                                                                                        888      
                                                                                        888      
                                                                                        
                                                                                        
  ```                                                                                      
                                                                                        
# Functionality
BlackIP-Rep accepts Bulk list of IP address which you need to check whether they are blacklisted or not, then BlackIP-Rep will check the list of IPs with Bulkblacklist.com and collect all the poor reputed IP or the Blacklisted ones and save that page as pdf for evidence. For further investigation proofs the tool will check the repution and take screenshot from Mxtoolbox or from Virustotal  for more evidence. The tool will also collect information such as the location, ASN, Service Provider of the list of IP provided.



# Requirements
```python
pip install -r requirements.txt
```

# Usage
```python
python3 BlackIP-Rep.py
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
<a href="https://github.com/sachinoliver/BlackIP-Rep/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=sachinoliver/BlackIP-Rep" />
</a>

