from output.models.saxon_data.override.over029_xsd.over029 import Order
from output.models.saxon_data.override.over029_xsd.over029 import ProductType
from output.models.saxon_data.override.over029_xsd.over029a import GiftWrap


obj = Order(
    product=ProductType(
        number=557,
        name='Short-Sleeved Linen Blouse',
        size=10,
        gift_wrap=GiftWrap(
            value='ADULT BDAY'
        ),
        points=100
    )
)
