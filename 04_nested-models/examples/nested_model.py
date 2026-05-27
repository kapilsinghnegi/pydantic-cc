from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    
class User(BaseModel):
    id: int
    name: str
    address: Address
    
# Forward referencing
class Comment(BaseModel):
    id: int
    content: str
    # self-replication / self-referencing
    replies: Optional[List['Comment']] = None 
    
Comment.model_rebuild()

address = Address(
    street = '123',
    city = 'Bareilly',
    postal_code = '243122'
)

user = User(
    id = 1,
    name = 'Kapil Negi',
    address = address,
)

comment = Comment(
    id = 1,
    content = 'First Comment',
    replies = [
        Comment(id = 2, content = 'Reply 1'),
        Comment(id = 3, content = 'Reply 2')
    ]
)