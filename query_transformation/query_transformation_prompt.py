from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from query_transformation.prompts import multiquery_template
from exception import MissingResourceError


class QueryTransformationPrompt:

    def __init__(self,template):
        self.prompt_template=ChatPromptTemplate.from_template(template)
        




class MultiQueryTransformationPrompt(QueryTransformationPrompt):
     def __init__(self,llm,query):
          super().__init__(template=multiquery_template)
          self.llm=llm
          self.user_query=query
          self.query_chain=None
          self.queries = None

     
     def generate_queries(self):
        if self.prompt_template==None:
            raise MissingResourceError('MultiQueryTransformation Template')
        
        if self.llm==None:
           raise MissingResourceError('LLM Model')
        
        if self.user_query==None:
            raise MissingResourceError('User Query')
        
        try:
            self.query_chain=(self.prompt_template | 
                    self.llm |
                    StrOutputParser() |
                    (lambda x : x.split("\n"))
                    )
            self.queries=self.query_chain.invoke(self.user_query)
        except Exception as e:
            raise MultiQueryTransformationPrompt(f"Message : {e}")
        
        return (self.query_chain, self.queries)

    
    

    
    
