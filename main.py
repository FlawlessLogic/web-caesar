from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
            <label for="rot">Rotate By: </label>
            <input id="rot" type="text" name="rot" value="0"/>
            <textarea id="text" name="text">{0}</textarea>
            <input type="submit" for="text"/>
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format('Text Goes Here')

@app.route("/encrypt", methods=['post'])

def encrypt():
    caesar_code = rotate_string(str(request.form['text']),int(request.form['rot']))
    
    return form.format(caesar_code)


app.run()