import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
class Generate_DALLE:
    def generateImage(input, size="1024x1024"):
        response = openai.Image.create(
            prompt=input,
            n=2,
            size=size
        )
        return response