from decimal import Decimal
from output.models.boeing_data.ipo6.ipo_xsd.address import Salutation
from output.models.boeing_data.ipo6.ipo_xsd.ipo import CustomerComment
from output.models.boeing_data.ipo6.ipo_xsd.ipo import ItemsType
from output.models.boeing_data.ipo6.ipo_xsd.ipo import PurchaseOrder
from output.models.boeing_data.ipo6.ipo_xsd.ipo import Ukaddress
from output.models.boeing_data.ipo6.ipo_xsd.itematt import ItemShipBy
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.models.datatype import XmlDate


obj = PurchaseOrder(
    salutation_or_extern_first_element=Salutation(
        value='Mrs.'
    ),
    ship_to_or_bill_to_or_single_address=[
        DerivedElement(
            qname='{http://www.example.com/IPO}singleAddress',
            value=Ukaddress(
                name='Helen Zoe',
                street='47 Eden Street',
                city='Cambridge',
                postcode='CB1 1JR'
            ),
            type='{http://www.example.com/IPO}UKAddress'
        ),
    ],
    customer_comment_or_ship_comment=CustomerComment(
        value='I love Boeing too!'
    ),
    items=ItemsType(
        content=[
            ItemsType.Item(
                product_name='777 Model',
                quantity=1,
                usprice=Decimal('99.95'),
                ship_date=XmlDate(1999, 12, 5),
                part_num='777-BA',
                weight_kg=Decimal('4.5'),
                ship_by=ItemShipBy.AIR
            ),
            ItemsType.Item(
                product_name='833 Model',
                quantity=1,
                usprice=Decimal('199.95'),
                ship_date=XmlDate(2000, 2, 28),
                part_num='833-AA'
            ),
        ]
    ),
    order_date=XmlDate(2002, 10, 20)
)
