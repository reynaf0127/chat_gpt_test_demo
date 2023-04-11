import gradio as gr 
import openai 

openai.api_key = openai.api_key = open("key.txt", "r"). read().strip('\n')

message_history = []

def predict (input): 
    global message_history
    message_history.append({"role": "user", "content": input})
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=message_history)
    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({"role":"assistant", "content": reply_content})
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(0,len(message_history)-1,2)]
    return response 


with gr.Blocks(css=".gradio-container {background:url('file=/home/yyc/Downloads/chatgpt_demo/download.png')}") as demo:
    chatbot = gr.Chatbot()
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder= "Type your message here").style(container=False)
        txt.submit(predict, txt, chatbot)
        txt.submit(None, None, txt, _js="()=>{''}")

demo.launch()



