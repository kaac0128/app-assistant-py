from flask import Flask, render_template, url_for, request
from flask_cors import CORS
from modules.Tools.Info import info_system
from modules.Notion_api_notes.notion_notes import Notes_Notion
from modules.Text_processing.message_process import TextProcessing
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/AssitantDB"
mongo = PyMongo(app)
db = mongo.db
cors = CORS(app, resources={r"/*": {"origins": "*"}})
notion = Notes_Notion()
process = TextProcessing()

@app.route('/index')
@app.route('/')
def index():
    datos = info_system();
    return render_template('index.html', datos = datos)

    
@app.route('/api/createPageNotion', methods=['POST'])
def createPageNotion():
    data = request.json['data'] 
    properties = {
        "Name": {"title": [{"text": {"content": f"{data.get('title', None)}"}}]},
        }
    children_page = [{"object": "block", "paragraph":{"rich_text":[{"text":{"content":f"{data.get('content', None)}"}}]}}]
    notion.create_page(properties=properties, children=children_page)
    return {"status":"ok"}
    
@app.route("/api/chatBrain", methods=['POST'])
def chatBrain():
    question = request.json['question'] 
    response = process.selectCommand(question)
    return response


@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='favicon.ico')


if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')