import socketserver
import http.server
import ssl
import json
import requests

def getResponse(user_input):
    return user_input

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        post_data = self.rfile.read(int(self.headers['Content-Length']))
        json_data = json.loads(post_data)

        chat_id = json_data['message']['from']['id']
        user_input = json_data['message']['text']

        bot_output = getResponse(user_input)

        url = "https://api.telegram.org/bot1318539129:AAEMoKJHN7ZyH40Y3tMNrHS_e0CcngD1lO4/sendMessage"

        r = requests.post(url = url, params = {'chat_id' : chat_id, 'text' : bot_output})
        if r.status_code == 200:
            self.send_response(200)
            self.end_headers() 

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

server = socketserver.TCPServer(('0.0.0.0', 8443), MyHandler)
server.socket = ssl.wrap_socket(server.socket)

server.serve_forever()
