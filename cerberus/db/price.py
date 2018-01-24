from py2neo import *

graph_db = neo4j.GraphDatabaseService()

class Price:
    def __init__(self, **kwargs):
        self.attrs = kwargs

    def save(self):
       self.cls.create(**self.attrs)

    @classmethod
    def create(cls, **kwargs):
       transaction = graph_db.begin(autocommit=True) 
       transaction.create(Node(f'{cls.__name__}', **kwargs)

    def all(cls):
        pass

    def first(cls):
        pass 

