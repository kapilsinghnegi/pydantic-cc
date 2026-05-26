from pydantic import BaseModel, Field, field_validator, computed_field

# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >=1)
# - rate_per_night: float
# Also, add computed field: total_amount = nights * rate_per_night

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights : int = Field(..., ge=1)
    rate_per_night: float
    
    # @field_validator('nights')
    # def nights_value(cls, value):
    #     if(value<1):
    #         raise ValueError("Nights cannot be less than 1")
    
    @computed_field
    @property
    def total_amount(self):
        return self.nights * self.rate_per_night