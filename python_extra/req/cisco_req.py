import requests
from requests.exceptions import HTTPError
from print_response import print_response


def main():

    api_path = "https://sandbox-sdwan-2.cisco.com/"
    requests.packages.urllib3.disable_warnings()

    credential = {
        "j_username": "devnetuser",
        "j_password": "RG!_Yw919_83"
    }
    sess = requests.Session()
    
    auth = sess.post(f"{api_path}/j_security_check",data=credential,verify=False)
    print("==>> auth: ", auth)
    
    breakpoint()
    
    if not auth.ok and auth.text:
        raise HTTPError("authentication failed")
    
    
    devices = sess.get(f"{api_path}dataservice/device",verify=False)
    devices.raise_for_status()
    print_response(devices,filename="get_cisco_sdwan_devices")
    # print("==>> devices: ", devices.json())
    
if __name__ == "__main__":
    main()