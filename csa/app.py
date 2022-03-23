#!/bin/env python
from notification import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    
    #CERT_FILE = "certificates/cert.pem"
    #KEY_FILE = "certificates/key.pem"

    socketio.run(app, port=8001, debug=True)
    #socketio.run(app, port=8000, debug=True, use_reloader=False, ssl_context=(CERT_FILE, KEY_FILE))