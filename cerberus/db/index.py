from py2neo import neo4j, node, rel
from cerberus.db.graph_base import GraphBase

graph_db = neo4j.GraphDatabaseService()

class Index(GraphBase):

    _root = graph_db.get_or_create_indexed_node("reference", "contracts", "root")


