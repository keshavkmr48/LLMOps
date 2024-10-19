import bs4
from langchain_community.document_loaders import WebBaseLoader

class DataLoader:
    def __init__(self):
        pass

class WebBaseDataLoader(DataLoader):

    def __init__(self, web_paths, content_class):
        super().__init__()
        self.web_paths=web_paths
        self.content_class=content_class
        self.loader=None
        self.docs=None

    def loading(self):
        self.loader = WebBaseLoader(
            web_paths=(self.web_paths,),
            # bs_kwarg = dict(
            #     parse_only=bs4.SoupStrainer(
            #         class_=self.content_class
            #     )
            # ),
        )

        self.docs=self.loader.load()
        return self.docs

