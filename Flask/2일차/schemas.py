from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(dump_only=True) #id 값은 서버에서 관리
    title = fields.String(required=True)
    author = fields.String(required=True)