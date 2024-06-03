# Python Keylogger
This basic keylogger written in Python uses the keyboard, socket, time, and os modules. On the host machine, start a Netcat listener on the defined port (3691). On the target machine, change the server variable to the host IP address and execute the Python file. The keylogger will send data every 10 seconds to the Netcat listener.
