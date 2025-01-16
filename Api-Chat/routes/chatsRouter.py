from flask import Blueprint, request, jsonify, Response
from openai import OpenAI
import os
import json


chats = Blueprint("chat", __name__)

@chats.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json
        print(user_input)

        if not user_input:
            print("El mensaje está vacío")
            return jsonify({"error": "El mensaje está vacío"}), 400

        formatted_messages = [
            {
                "role": "system",
                "content": "Te llamas ChatBot y debes responder las preguntas que te hagan",
            }
        ]

        # Agregar los mensajes del usuario y del asistente
        for message in user_input["messages"]:
            print(f"Agregando mensaje del usuario {message['role']}: {message['content']}")
            formatted_messages.append({"role": message["role"], "content": message["content"]})
            

        client = OpenAI()
        # Solicitar respuesta a OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=formatted_messages,
            max_tokens=100,
            temperature=0.2,
            stream=True,
        )


        def generate():
            for chunk in response:
               
                if chunk.choices[0].delta.content:
                    """ print(f"Generando respuesta: {chunk.choices[0].delta.content}") """
                    yield f"data: {json.dumps({'content': chunk.choices[0].delta.content,
                    'status': 'streaming'})}\n\n"
                    

                if chunk.choices[0].finish_reason == "stop":
                    print("Terminando la generación")
                    yield f"data: {json.dumps({'status': 'done'})}\n\n"
                    break

            

        return Response(generate(), mimetype="text/event-stream")
        
       

    except Exception as e:
        print(f"Chat request failed: {str(e)}")
        return jsonify({"error": str(e)}), 500