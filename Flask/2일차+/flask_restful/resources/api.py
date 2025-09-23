from flask import request
from flask_restful import Resource

items = [{"name":"choi", "price":8000}]

class Item(Resource):

    def get(self, name):
        for item in items:
            if name == item.get("name"):
                return item
        return {"msg":"항목이 없습니다."}, 404

    
    def post(self, name):
        data = request.get_json()
        for item in items:
            if name == item.get("name"):
                return {"mag":"이미 있는 상품입니다."}, 403
        items.append({"name":name, "price":data.get("price")})
        return {"msg":f"{name}이 추가 되었습니다."}

    def put(self, name):
        data = request.get_json()
        for item in items:
            if name == item.get("name"):
                item["price"] = data.get("price")
                return {"msg":f"{name}의 price:{data}로 변경"}
        items.append({"name":name, "price":data.get("price")})
        return {"msg":f"{name}이 추가 되었습니다."}
    
    def delete(self, name):
        for item in items:
            if name == item.get("name"):
                items.remove(item)
        return f"{name} 삭제 되었습니다."