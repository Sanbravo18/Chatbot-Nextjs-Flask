from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de OpenAI API


app = Flask(__name__)
CORS(app)  # Habilitar CORS


@app.route("/chat", methods=["POST"])

def chat():
    try:
        user_input = request.json
        print(user_input)
        

        if not user_input:
            print("El mensaje está vacío")
            return jsonify({"error": "El mensaje está vacío"}), 400

        messages = [
                {
                    "role": "system",
                    "content": "Te llamas ChatBot y debes responder las preguntas que te hagan",
                }
            ]
            
       

        # Agregar los mensajes del usuario
        for message in user_input["messages"]:
            print(f"Agregando mensaje del usuario")
            messages.append({"role": "user", "content": message["content"]})

        client = OpenAI()
         # Solicitar respuesta a OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=100,
            temperature=0.2,
        )

        assistant_message = response.choices[0].message

        
        print("respuesta del usuario")
        print(user_input)
        print("Respuesta del asistente")
        print(assistant_message.content)
        return jsonify({"response": assistant_message.content})
    

    except Exception as e:
        print(f"Chat request failed: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)

