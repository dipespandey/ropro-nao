from flask import request, render_template
from flask import Flask
from services.nao_services import speak, move_a_little

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def say_something( ):
    if request.method == 'POST':
        text = request.form.get('input_text')
        move = request.form.get('move')
        if move:
            print("button is", move)
            move_a_little(0.2)
        elif text:
            print("text is", text)
            speak(text)
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(port=5001)