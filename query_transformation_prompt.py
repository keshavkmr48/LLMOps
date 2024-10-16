from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.load import dumps, loads
from LLMOPS.query_transformation.prompts import multiquery_template
print(multiquery_template)

class QueryTransformationPrompt:

    def __init__(self,template):
        self.prompt_template=ChatPromptTemplate.from_template(template)
        self.queries = None

    def generate_queries(self):
        pass







class MultiQueryTransformationPrompt(QueryTransformationPrompt):
     def __init__(self):
          super().__init__(multiquery_template)

    


def generate_queries(self, query):
        query_chain=(self.prompt_template | 
                ChatGroq(temperature=0) |
                StrOutputParser())
        self.queries=query_chain.invoke(query)
        return self.queries
    

    
    
