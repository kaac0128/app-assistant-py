from youdotcom import Chat, Search, Code, Write
import os

YOU_APIKEY = os.getenv("YOU_APIKEY")
class You_data:
    def chatYou(self, input):
        data = Chat.send_message(message=input, api_key=YOU_APIKEY)
        return data
    
    def codeGenerate(self, input):
        text = Code.gen_code("python loop")
        return text
    
    def searchYou(self, input):
        search_results = Search.search_for(input)
        return search_results
    
    def writeYou(self, input):
        text = Write.write(input)
        return text