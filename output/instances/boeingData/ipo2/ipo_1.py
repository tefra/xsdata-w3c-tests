from decimal import Decimal
from output.models.boeing_data.ipo2.ipo_xsd.address import Usaddress
from output.models.boeing_data.ipo2.ipo_xsd.address import Usstate
from output.models.boeing_data.ipo2.ipo_xsd.ipo import Comment
from output.models.boeing_data.ipo2.ipo_xsd.ipo import CustomerComment
from output.models.boeing_data.ipo2.ipo_xsd.ipo import ItemShipBy
from output.models.boeing_data.ipo2.ipo_xsd.ipo import ItemsType
from output.models.boeing_data.ipo2.ipo_xsd.ipo import PurchaseOrder
from output.models.boeing_data.ipo2.ipo_xsd.ipo import ShipComment
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.models.datatype import XmlDate


obj = PurchaseOrder(
    ship_to_or_bill_to_or_single_address=[
        DerivedElement(
            qname='shipTo',
            value=Usaddress(
                name='Alice Smith',
                street='123 Maple Street',
                city='Mill Valley',
                state=Usstate.CA,
                zip=90952
            ),
            type='{http://www.example.com/add}USAddress'
        ),
        DerivedElement(
            qname='billTo',
            value=Usaddress(
                name='Robert Smith',
                street='8 Oak Avenue',
                city='Old Town',
                state=Usstate.PA,
                zip=95819
            ),
            type='{http://www.example.com/add}USAddress'
        ),
    ],
    customer_comment_or_ship_comment_or_comment=Comment(
        value='Hurry, my sister loves Boeing!'
    ),
    items=ItemsType(
        content=[
            ItemsType.Item(
                product_name='777 Model',
                quantity=1,
                usprice=Decimal('99.95'),
                customer_comment_or_ship_comment_or_comment=[
                    ShipComment(
                        value=' Use gold wrap if possible '
                    ),
                    CustomerComment(
                        value=' Want this for the holidays! '
                    ),
                ],
                ship_date=XmlDate(1999, 12, 5),
                part_num='777-BA',
                weight_kg=Decimal('4.5'),
                ship_by=ItemShipBy.AIR
            ),
            ItemsType.Item(
                product_name='833 Model',
                quantity=2,
                usprice=Decimal('199.95'),
                customer_comment_or_ship_comment_or_comment=[
                    Comment(
                        value='This is a comment...'
                    ),
                ],
                ship_date=XmlDate(2000, 2, 28),
                part_num='833-AA',
                weight_kg=Decimal('2.5'),
                ship_by=ItemShipBy.AIR
            ),
        ]
    ),
    order_date=XmlDate(2002, 10, 20)
)
