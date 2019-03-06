"""
This script runs the qmeter application using a development server.
"""

from os import environ
from app import create_app

if __name__ == '__main__':
    app = create_app()

#HOST = environ.get('SERVER_HOST', 'localhost')
#try:
#    PORT = int(environ.get('SERVER_PORT', '5555'))
#except ValueError:
#    PORT = 5555
#app.run(HOST, PORT)
