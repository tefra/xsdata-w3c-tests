from decimal import Decimal
from output.models.ms_data.additional.ipo_s1_xsd.ipo_s1 import Comment
from output.models.ms_data.additional.ipo_s1_xsd.ipo_s1 import Items
from output.models.ms_data.additional.ipo_s1_xsd.ipo_s1 import PurchaseOrder
from output.models.ms_data.additional.ipo_s1_xsd.ipo_s1_address import Address
from xsdata.models.datatype import XmlDate


obj = PurchaseOrder(
    ship_to=Address(
        name='Helen Zoe',
        street='47 Eden Street',
        city='Cambridge'
    ),
    bill_to=Address(
        name='Robert Smith',
        street='8 Oak Avenue',
        city='Old Town'
    ),
    items=Items(
        item=[
            Items.Item(
                product_name='Lapis necklace',
                quantity=1,
                usprice=Decimal('99.95'),
                comment=Comment(
                    value='Want this for the holidays!'
                ),
                ship_date=XmlDate(1999, 12, 5),
                part_num='833-AA'
            ),
        ]
    ),
    order_date=XmlDate(1999, 12, 1)
)
