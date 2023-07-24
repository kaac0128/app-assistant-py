import dotenv

from langchain.chat_models import ChatOpenAI
#from langchain.prompts.chat import (
#    ChatPromptTemplate,
#    SystemMessagePromptTemplate,
#    HumanMessagePromptTemplate,
#)
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.output_parsers import StructuredOutputParser
from modules.roles_templates.roles_templates import roles_template
from modules.schemas.brain_schema import response_schemas
from langchain.llms import OpenAI

dotenv.load_dotenv()
llm = OpenAI(temperature=0.5)
tools = load_tools(["google-serper"], llm=llm)
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

class LangChainBrainAssitant:
    def __create_chain(self):
        prompt_template = roles_template.get("prompt_template")
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["input"]
        )
        return LLMChain(llm=llm, prompt=prompt)
    
    def __create_agent(self):
        return initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )
    
    def chat(self, input):
        agent = self.__create_agent()
        chain = self.__create_chain()
        overall_chain = SimpleSequentialChain(
            chains=[agent, chain],
            verbose=True
        )
        response = overall_chain.run(input)
        return output_parser.parse(response)