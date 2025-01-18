from flask import Flask

from flask_cors import CORS


from dotenv import load_dotenv

from routes.usersRouter import users 
from routes.chatsRouter import chats

# Cargar variables de entorno
load_dotenv()

# Configuración de OpenAI API

app = Flask(__name__)
CORS(app)  # Habilitar CORS
app.register_blueprint(users)
app.register_blueprint(chats)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
