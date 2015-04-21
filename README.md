# vSphere Port Scan
Automatically scan all TCP and UDP Ports required to access VMware vCenter Server, VMware ESXi and ESX hosts to determine their status (open or blocked).

For a detailed explanation of the work put into the script so far check out the new Python Series on Datacenterdude.com.

*All port information pulled from [VMware KB 1012382](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1012382)*

## Supported vSphere Objects

* vCenter 5.x
* ESXi 5.x

## Features in Development 

* ~~Scan ESXi and vCenter separately~~
* Manually enter multiple IP addresses for ESXi
* Scan multiple vCenter servers
* Enable the ability to export a list of the affected ports

