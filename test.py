from flask import Flask, render_template, request
import openai 

app = Flask(__name__)

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


@app.route('/', methods=['GET', 'POST'])
def home():
    output_text = ""
    if request.method == 'POST':
        input_text = request.form['input_text']
        output_text = predict(input_text) # modify the input text as desired
        
    return render_template('chat.html', output_text=output_text)

if __name__ == '__main__':
    app.run(debug=True)
