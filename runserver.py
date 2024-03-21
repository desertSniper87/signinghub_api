import os
from example_app.example_app import app

# Start a Flask development server with SSL support
if __name__ == "__main__":
    # Optional HTTPS Server
    ssl_context = (app.root_path+'/server.crt', app.root_path+'/server.key')
    print("Point your browser to https://localhost:443")
    print("Notice the 's' in 'https' and the 443 port instead of the usual 80")
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=ssl_context)
    # Optional HTTPS Server

    # Normal HTTP Server
    # app.run(host='0.0.0.0',port=80, debug=True)

