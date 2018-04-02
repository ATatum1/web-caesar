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
        <form action="/" method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot">
            </div>
            
                
                <textarea type="text" name="text"></textarea>     
            
            
                <input type="submit" name="Submit">
        </form>
       
    </body>

    
</html>



"""



@app.route("/")
def index():
    return form


@app.route("/", methods=["post"])
def encrypt():
   
    rot = request.form["rot"] #int(rot)
    rot =int(rot)
    #text = request.form['text']
    text = request.form["text"]
    rotate_text = rotate_string(text,rot)
    return  '<h1>' + rotate_text + '</h1>'

  
app.run()

#encrypt(rot,text)