from output.models.saxon_data.override.over029_xsd.over029 import Order
from output.models.saxon_data.override.over029_xsd.over029 import ProductType


obj = Order(
    product=ProductType(
        number=557,
        name="Short-Sleeved Linen Blouse",
        size=10,
        gift_wrap="ADULT BDAY",
        points=100
    )
)
