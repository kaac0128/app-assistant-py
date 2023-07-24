from flask import Flask, render_template, url_for, request
from modules.Tools.Apps import vsc_open
from modules.Tools.Info import greet_user, get_ip
from modules.Tools.Message import send_whatsapp_message
from flask_cors import CORS
from modules.Notion_api_notes.notion_notes import Notes_Notion
from modules.langchain_assitant.langchain_brain import LangChainBrainAssitant
from modules.Generator_images.OpenAI_DallE import Generate_DALLE
from modules.You_opcions.you_chat import You_data
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/AssitantDB"
mongo = PyMongo(app)
db = mongo.db
cors = CORS(app, resources={r"/*": {"origins": "*"}})
notion = Notes_Notion()
langChatBrain = LangChainBrainAssitant()
generateImages = Generate_DALLE()
youService = You_data()


@app.route('/index')
@app.route('/')
def index():
    welcome = greet_user();
    return render_template('index.html')

@app.route('/actionVsc')
def vscOpen():
    return vsc_open()

@app.route('/welcome')
def greetUser(): 
    return greet_user()

@app.route('/getIp')
def getIp():
    return get_ip()

@app.route('/searchWiki', methods=['POST'])

@app.route('/sendMessageWhatsapp', methods=['POST'])
def sendWhatsappMessage():
    number = request.json['number'] 
    message = request.json['message'] 
    send_whatsapp_message(number, message)
    
@app.route('/api/createPageNotion', methods=['POST'])
def createPageNotion():
    data = request.json['data'] 
    properties = {
        "Name": {"title": [{"text": {"content": f"{data.get('title', None)}"}}]},
        }
    children_page = [{"object": "block", "paragraph":{"rich_text":[{"text":{"content":f"{data.get('content', None)}"}}]}}]
    notion.create_page(properties=properties, children=children_page)
    
@app.route("/api/chatBrain", methods=['POST'])
def chatBrain():
    question = request.json['question'] 
    response = langChatBrain.chat(question)
    return response

@app.route("/api/generateCode", methods=['POST'])
def generateCode():
    question = request.json['question'] 
    response = youService.codeGenerate(question)
    return response

@app.route("/api/youChat", methods=['POST'])
def youChat():
    question = request.json['question'] 
    response = youService.chatYou(question)
    return response

@app.route("/api/youSearch", methods=['POST'])
def youSearch():
    question = request.json['question'] 
    response = youService.searchYou(question)
    return response

@app.route("/api/youWrite", methods=['POST'])
def youWrite():
    question = request.json['question'] 
    response = youService.writeYou(question)
    return response
    
@app.route("/api/generateImagesAI", methods=['POST'])
def generateImagesAI():
    question = request.json['question'] 
    response = generateImages.generateImage(question)
    return response

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='favicon.ico')


if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')