from flask import Flask, render_template, request
from netmiko import ConnectHandler

app = Flask(__name__)

ROUTER_IP = '192.168.10.102'
ROUTER_PORT = 32770

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    error = None

    if request.method == 'POST':
        router_device = {
            'device_type': 'cisco_ios_telnet',
            'ip': ROUTER_IP,
            'port': ROUTER_PORT,
            'username': 'admin',
            'password': 'eve123',
            'secret': 'eve123',
        }

        commands_to_run = [
            'show ip interface brief',
            'show version',
            'show running-config',
        ]

        try:
            with ConnectHandler(**router_device) as net_connect:
                net_connect.enable()

                results = {}
                for command in commands_to_run:
                    results[command] = net_connect.send_command(command)

        except Exception as e:
            error = f"Connection failed: {e}"

    return render_template(
        'index.html',
        target=f"{ROUTER_IP}:{ROUTER_PORT}",
        results=results,
        error=error,
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)