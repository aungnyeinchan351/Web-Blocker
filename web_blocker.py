import pyfiglet
import os
import platform
os.system("clear")
print(pyfiglet.figlet_format("Web Blocker"))
Windows_Path = "C:\Windows\System32\drivers\etc\hosts"
Linux_Path = "/etc/hosts"
mac_path = "/etc/hosts"
if platform.system() == "Linux":
    path = Linux_Path
elif platform.system() == "Windows":
    path = Windows_Path
elif platform.system() == "Darwin":
    path = mac_path
redirect = "127.0.0.1"
sites_to_block = []
print("Enter Websites to block. Enter (0) to stop.")
sites = input()
while sites != "0":
    sites_to_block.append(sites)
    sites = input()
print("What do you want to do?\n1. Block  2. Unblock")
decision = int(input())
if decision == 1:
    with open(path,'r+') as file:
            content=file.read()
            for site in sites_to_block:
                if site in content:
                    pass
                else:
                   file.write(redirect+" "+site+"\n")
    print("Success!")

elif decision == 2:
    with open(path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites_to_block):
                    file.write(line)
            file.truncate()
    print("Success!")
else:
    print("Invalid input")            