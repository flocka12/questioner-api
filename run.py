import os

from app import create_app

CONFIG_NAME = os.getenv('APP_SETTINGS')

app = create_app(CONFIG_NAME)

if __name__ == "__main__":
    app.run()
