import requests
import json
import yaml
import rich
import warnings
from getpass import getpass
from requests.auth import HTTPBasicAuth

class MyError(Exception):
    """Custom base class for exceptions"""
    pass

class AuthenticationError(MyError):
    """To be raised when authentication failure occurs"""
    pass

def get_token_for_dnac(ip_address, username, password):
    """ function to get a valid token for DNAC API
    access. Input needed is DNAC IP address, username
    and password
    """

    # build complete URL first

    token_url = "https://" + ip_address + "/dna/system/api/v1/auth/token"

    # use a POST call to get token

    warnings.filterwarnings("ignore")
    token_call = requests.post(token_url, auth=HTTPBasicAuth(username, password), headers={"Content-Type": "application/json"}, verify=False)

    # return actual token

    return(token_call.json()['Token'])

def get_network_devices_from_dnac(ip_address, token):
    """ function to get complete list of network
    devices from DNAC using DNACs IP address and 
    the authentication token as an input
    """

    # build complete URL first

    network_device_url = "https://" + ip_address + "/dna/intent/api/v1/network-device/"

    # use a GET call to return this data

    network_device_call = requests.get(network_device_url, headers={"Content-Type":"application/json", "X-Auth-Token": token}, verify=False)
    
    # return network device list

    return(network_device_call.json()['response'])

def parse_device_list(device_list):
    """ parse through device list returned
    from DNAC and save it in a new dictionary with
    relevant information only
    """

    parsed_device_list = {}

    # loop through device list and store information
    # in a temporary dictionary

    for device in device_list:

        temp_dict = {}

        device_hostname = device['hostname']
        temp_dict = {device_hostname: {
            'hostname': device['managementIpAddress'],
            'groups': [device['role'].lower()]}
            }

        parsed_device_list.update(temp_dict)

    return parsed_device_list

def main():
    dnac_ip_address = input("Enter the IP address for DNAC: ")
    dnac_username = input("Enter username for DNAC: ")
    dnac_password = getpass("Enter password for DNAC: ")

    # try to get valid token for DNAC now

    try:
        token = get_token_for_dnac(dnac_ip_address, dnac_username, dnac_password)
        rich.print("[green]Retrieved token from DNAC for subsequent API calls")
    except:
        raise AuthenticationError("Error getting token for DNAC. Please try again with correct credentials\n")

    # get username/password for network devices along with 
    # list of network devices from DNAC

    rich.print("[blue]\n=============================================\n")
    device_username = input("Enter the username for network devices: ")
    device_password = getpass("Enter the password for network devices: ")

    dnac_device_list = get_network_devices_from_dnac(dnac_ip_address, token)

    # device list could be empty if no devices are present in DNAC
    # return if empty

    if dnac_device_list:
        rich.print("[green]Retrieved device list from DNAC")
    else:
        rich.print("[red]No devices found in DNAC inventory")
        return

    # parse through device list to build nornir hosts file

    rich.print("[blue]\n=============================================\n")
    hosts_dict = parse_device_list(dnac_device_list)

    # convert hosts file into yaml and save it in user specified directory

    try:
        hosts_file_path = input("Please enter complete path where Nornir hosts file should be saved: ")
        rich.print("[green]Attempting to create Nornir hosts file")
        hosts_file = open(hosts_file_path, "w")
        hosts_file.write("---\n\n")
        yaml.dump(hosts_dict, hosts_file)
        hosts_file.close()
        rich.print("[green]Created Nornir hosts file")
    except:
        rich.print("[red]Could not open file. Check path and/or file, directory permissions")
        return

    # create a defaults.yaml for Nornir for common connection options

    rich.print("[blue]\n=============================================\n")

    try:
        defaults_file_path = input("Please enter complete path where Nornir defaults file should be saved: ")
        rich.print("[green]Attempting to create Nornir defaults file")

        # initialize the nested dictionary first

        defaults_dict = {'connection_options': {'scrapli': {}}}
        defaults_dict['username'] = device_username
        defaults_dict['password'] = device_password

        # this code currently supports iosxe only
        # assign scrapli parameters for iosxe login

        defaults_dict['connection_options']['scrapli']['platform'] = 'cisco_iosxe'
        defaults_dict['connection_options']['scrapli']['port'] = 22
        defaults_dict['connection_options']['scrapli']['extras'] = {}
        defaults_dict['connection_options']['scrapli']['extras']['auth_strict_key'] = False

        # open file and write to it now

        defaults_file = open(defaults_file_path, "w")
        defaults_file.write("---\n")
        yaml.dump(defaults_dict, defaults_file)
        defaults_file.close()
        rich.print("[green]Created Nornir defaults file")
    except:
        rich.print("[red]Could not open file. Check path and/or file, directory permissions")
        return

if __name__ == "__main__":
    main()


