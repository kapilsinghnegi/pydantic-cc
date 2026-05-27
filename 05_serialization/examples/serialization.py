from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zipcode: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []
    
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )
    
# create a user instance
user = User(
    id = 1,
    name = "Tommy Vercetti",
    email = 'vercetti@vc.com',
    created_at = datetime(2026, 5, 27, 17, 30),
    is_active = True,
    address = Address(
        street = "123",
        city = "Vice City",
        zipcode = "001"
    ),
    tags = ['premium', 'subscriber']
)

# Using model_dump() -> dict
python_dict = user.model_dump()
print(python_dict)

print('*'*120)

# Using model_dump_json()
json_str = user.model_dump_json()
print(json_str)
