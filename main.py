from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px
                font: 16px sans-serif;
                border_radiusd: 10px;
            }

            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form action="/caesar" method="post">
            <div>
                <label for="rotate">Rotate by:</label>
                <input type="text" id="rotate" name="rot">
            </div>
            <div>
                <label for="msg"></label>
                <textarea id="msg" name="text" name=""></textarea>
            </div>
            <div>
                <input type="button" value="Submit">
            </div>
   
    </body>
</html>

"""
@app.route("/")
def index():
    return form


@app.route("/", methods=['POST'])
def encrypt(rot,text):
    rotation = int(rot)
    text_input = request.form['text_input']
    rotate_text = rotate_string(rotation,text_input)
    return '<h1>' + rotate_text + '</h1>'

  


    app.run()