from flask import Flask
import utils
app = Flask(__name__)


@app.route("/scores")
def score_server():
    read_file = open(utils.SCORES_FILE_NAME, 'r')
    for line in read_file.readlines():
        score = line
    read_file.close()
    return """
   <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">"""+score+"""</div></h1>
        </body>
   </html>
        """



@app.route("/error")
def error():
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1><div id="score" style="color:red">"""+str(utils.BAD_RETURN_CODE)+"""</div></h1>
        </body>
    </html>
        """

app.run(port=5000)
