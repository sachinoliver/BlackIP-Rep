# BlackIP-Rep
BlackIP-Rep is a tool designed to gather the reputation and information of Blacklisted IP's. The tool will collect evidence from major spamlists. The tool is mainly is focused on increasing the workflow of Security Operations(SOC) team during investigation. 
                                                                                    
                                                                                        
## Functionality
BlackIP-Rep accepts Bulk list of IP address which you need to check whether they are blacklisted or not, then BlackIP-Rep will check the list of IPs with Bulkblacklist.com and collect all the poor reputed IP or the Blacklisted ones and save that page as pdf for evidence. For further investigation proofs the tool will check the repution and take screenshot from Mxtoolbox or from Virustotal  for more evidence. The tool will also collect information such as the location, ASN, Service Provider of the list of IP provided.



## Requirements
```python
pip install -r requirements.txt
```

## Usage
```python
python3 BlackIP-Rep.py filethatcontainsips.txt
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

