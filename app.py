#Desclaramos las dependencias a usar
import openai
import gradio as gr

#Definimos valor de API key
openai.api_key = "INSERTA_TU_API_KEY_AQUI"

#Establecemos constantes
messages = [
    {"role": "system", "content": "PARAMETROS DE FUNCION"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "system", "content": reply})
        return reply

#Generamos la interfaz con gradio
inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Argan GPT",
             description="IA especializada en emprendimiento",
             theme="compact").launch(share=True)
