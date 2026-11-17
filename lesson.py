from netmiko import ConnectHandler

router_device = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.10.102',
    'port': 32770,
    'username': 'admin',
    'password': 'eve123',
    'secret': 'eve123',

}

try:
    print("Connecting to the router...")
    net_connect = ConnectHandler(**router_device)

    # Elevate to Privileged EXEC mode (R1#)
    net_connect.enable()

    # 1. Define your commands in a list
    commands_to_run = [
        'show ip interface brief',
        'show version',
        'show running-config'
    ]

    # 2. Loop through the list to execute them one by one
    for command in commands_to_run:
        print(f"\n--- Output for {command} ---")
        output = net_connect.send_command(command)
        print(output)

    net_connect.disconnect()
    print("\nDisconnected successfully.")
except Exception as e:
    print(f"Connection failed: {e}")