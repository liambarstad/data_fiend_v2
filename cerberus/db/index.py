from py2neo import neo4j, node, rel
from cerberus.db.price import Price

graph_db = neo4j.GraphDatabaseService()

class Index(Price):

    _root = graph_db.get_or_create_indexed_node("reference", "contracts", "root")


