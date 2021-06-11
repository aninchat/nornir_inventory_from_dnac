# nornir_inventory_from_dnac
**Creating a Nornir network inventory from Cisco DNA Center**

A sample of the hosts.yaml and the defaults.yaml file that is generated from this script is stored in the 'Sample' folder, along with manually created config.yaml and group.yaml files. A simple Nornir script is also in there to confirm that the hosts and defaults file generated from the script actually works with Nornir. 

**Example usage of nornir inventory script:**

```
(Nornir2.5) aninchat@aninchat-ubuntu:~/Automation/Python/Nornir2.5_Projects$ python create_nornir_inventory_from_dnac.py 
Enter the IP address for DNAC: 10.104.233.91
Enter username for DNAC: admin
Enter password for DNAC: 
Retrieved token from DNAC for subsequent API calls

=============================================

Enter the username for network devices: aninchat
Enter the password for network devices: 
Retrieved device list from DNAC

=============================================

Please enter complete path where Nornir hosts file should be saved: /home/aninchat/Automation/Python/Nornir2.5_Projects/Sample/hosts.yaml
Attempting to create Nornir hosts file
Created Nornir hosts file

=============================================

Please enter complete path where Nornir defaults file should be saved: /home/aninchat/Automation/Python/Nornir2.5_Projects/Sample/defaults.yaml
Attempting to create Nornir defaults file
Created Nornir defaults file
```

**Output of the 'sample_nornir_script' (as an example):**

```
(Nornir2.5) aninchat@aninchat-ubuntu:~/Automation/Python/Nornir2.5_Projects/Sample$ python sample_nornir_script.py 
send_command********************************************************************
* HQ-Border1.tatooine.com ** changed : False ***********************************
vvvv send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
  Name                             Default RD            Protocols   Interfaces
  Group1                           1:4101                ipv4        Lo1021
                                                                     Vl3001
                                                                     LI0.4101
  Group2                           1:4099                ipv4        Vl3002
                                                                     LI0.4099
  Group3                           1:4100                ipv4        Vl3003
                                                                     LI0.4100
  Mgmt-vrf                         <not set>             ipv4,ipv6   Gi0/0

  Platform iVRF Name               iVRF Id               Interfaces
  __Platform_iVRF:_ID00_           0                     LI3/2
^^^^ END send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* HQ-Border2.tatooine.com ** changed : False ***********************************
vvvv send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
  Name                             Default RD            Protocols   Interfaces
  Group1                           1:4101                ipv4        Lo1021
                                                                     Vl3005
                                                                     LI0.4101
  Group2                           1:4099                ipv4        Vl3006
                                                                     LI0.4099
  Group3                           1:4100                ipv4        Vl3007
                                                                     LI0.4100
  Mgmt-vrf                         <not set>             ipv4,ipv6   Gi0/0

  Platform iVRF Name               iVRF Id               Interfaces
  __Platform_iVRF:_ID00_           0                     LI3/2
^^^^ END send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* HQ-Edge-1.tatooine.com ** changed : False ************************************
vvvv send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
  Name                             Default RD            Protocols   Interfaces
  Group1                           <not set>             ipv4        LI0.4101
                                                                     Vl1021
  Group2                           <not set>             ipv4        LI0.4099
  Group3                           <not set>             ipv4        LI0.4100
  Mgmt-vrf                         <not set>             ipv4,ipv6   Gi0/0
^^^^ END send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* HQ-Edge-2.tatooine.com ** changed : False ************************************
vvvv send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
  Name                             Default RD            Protocols   Interfaces
  Group1                           <not set>             ipv4        LI0.4101
                                                                     Vl1021
  Group2                           <not set>             ipv4        LI0.4099
  Group3                           <not set>             ipv4        LI0.4100
  Mgmt-vrf                         <not set>             ipv4,ipv6   Gi0/0
^^^^ END send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
