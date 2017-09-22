
from flask import Flask, request, redirect
from caesar import rotate_string 

app = Flask(__name__)
app.config['DEBUG'] = True


form= """
<!DOCTYPE html>

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
                margin: 10px 1  0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method='POST'>
        <label> Rotate By:
        <input type="text" ID="rot" name="rot" value="0" />
        </label><br>
        <textarea type="text" name="text">{0}</textarea>
        <input type ="submit" name="submit Query"/>
        </body>
</html>
"""
@app.route('/')
def index():
    return form.format("")
#    return form
     
@app.route('/', methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    text = rotate_string(text,rot)
    text = "{0}".format(text)
    return form.format(text)

app.run()