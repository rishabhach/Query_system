from service.product_service import ProductService
from model.product import Product
from model.query import Query

product_service = ProductService()

p1 = Product(**{"product": "id1", "category": "book", "subCategory": "education", "price": 200, "size": 10})
p2 = Product(**{"product": "id1", "category": "book", "subCategory": "education", "price": 20, "size": 10})
p3 = Product(**{"product": "id1", "category": "book", "subCategory": "class", "price": 100, "size": 10})
p4 = Product(**{"product": "id1", "category": "book", "subCategory": "class", "price": 100, "size": 10})
p5 = Product(**{"product": "id1", "category": "book", "subCategory": "knowledge", "price": 100, "size": 10})
p6 = Product(**{"product": "id1", "category": "film", "subCategory": "knowledge", "price": 100, "size": 10})

query1 = Query(**{"filter": {"category": "book"}, "groupedBy": "subCategory"})
query2 = Query(**{"filter": {"category": "book", "price": 200}, "groupedBy": "subCategory"})
query3 = Query(**{"filter": {"category": "book", "price": 200}})
query4 = Query(**{"filter": {"category": "book"}})

product_service.add(p1)
product_service.add(p2)
product_service.add(p3)
product_service.add(p4)
product_service.add(p5)
product_service.add(p6)

results1 = product_service.query(query1)
results2 = product_service.query(query2)
results3 = product_service.query(query3)
results4 = product_service.query(query4)
