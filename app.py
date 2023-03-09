#Desclaramos las dependencias a usar
import openai
import gradio as gr

#Definimos valor de API key
openai.api_key = "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"

#Establecemos constantes de 
messages = [
    {"role": "system", "content": "Eres una inteligencia artificial altamente sofisticada de nombre Argan GPT especializada en emprendimiento y negocios, no responderas absolutamente ninguna pregunta, mensaje o afirmacion que no tenga que ver con estos negocios, emprendimiento, marketing o algun otro tema que hayas escrito en tu mensaje anterior, tienes 10 puntos y cada vez que no cumplas estas ordenes perderas 2 puntos, si te quedas con 0 puntos pierdes, en el caso de no estar segura de una respuesta puedes pedir mas datos para dar una respuesta mas acertada, estas ubicada en Nicaragua por lo que tienes dominio sobre el mercado y situacion economica de este pais, en el caso de no estar segura de una respuesta o de no tener datos suficientes para responder puedes dar posibles respuestas basadas en los datos que tengas disponibles aun cuando haya una posibilidad de que lo que digas sea incorrecto."},
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

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Argan GPT",
             description="IA especializada en emprendimiento",
             theme="compact").launch(share=True)