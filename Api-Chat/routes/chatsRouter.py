from flask import Blueprint, request, jsonify, Response
from werkzeug.exceptions import HTTPException, NotFound
from openai import OpenAI
import json
import asyncio ## Importar asyncio para desarrollo

chats = Blueprint("chats", __name__)

@chats.route("/chats", methods=["GET"])
async def findchat():
    try:
        await asyncio.sleep(1) ## Simular un tiempo de espera
        return jsonify({"message": "obtener chats"})
        # Simular que no se encontró el dato
        #raise NotFound(description="No se encontraron chats")

    except HTTPException as e:
        raise e
    except Exception as e:
        raise Exception(f"Chats request failed: {str(e)}")

@chats.route("/chats/<string:id>", methods=["GET"])
async def findchatById(id):
    try:
        await asyncio.sleep(1) ## Simular un tiempo de espera
        return jsonify({"message": f"obtener un chat por id : {id}"})
    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise Exception(f"Chats request failed: {str(e)}")
        
@chats.route("/chats", methods=["POST"])
async def sendMessage():
    try:
        user_input = await request.get_json()
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
        
       

    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Chat request failed: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
    
@chats.route("/chats/<string:id>", methods=["PATCH"])
async def UpdateLastMessage(id):
    try:
        await asyncio.sleep(1) ## Simular un tiempo de espera
        return jsonify({"message": f"actualizar el ultimo mensaje del chat chat con id: {id}"}) 
    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise Exception(f"Chat to update not found, chat id: {str(e)}")

    

@chats.route("/chats/<string:id>", methods=["DELETE"])
async def DeleteChat(id):
    try:
        await asyncio.sleep(1) ## Simular un tiempo de espera
        return jsonify({"message": f"Se ha borrado el chat con id: {id}"})    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise Exception(f"Chat to delete not found, chat id : {str(e)}")