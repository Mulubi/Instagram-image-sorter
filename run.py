import os

from Flask_IIS import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)