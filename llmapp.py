from flask import Flask, request, render_template
from llm_utils import ask_openai

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        user_input = request.form['prompt']
        response = ask_openai(user_input)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)