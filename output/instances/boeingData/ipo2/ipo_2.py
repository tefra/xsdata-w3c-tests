from decimal import Decimal
from output.models.boeing_data.ipo2.ipo_xsd.address import Ukaddress
from output.models.boeing_data.ipo2.ipo_xsd.ipo import ItemShipBy
from output.models.boeing_data.ipo2.ipo_xsd.ipo import ItemsType
from output.models.boeing_data.ipo2.ipo_xsd.ipo import PurchaseOrder
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.models.datatype import XmlDate


obj = PurchaseOrder(
    ship_to_or_bill_to_or_single_address=[
        DerivedElement(
            qname="singleAddress",
            value=Ukaddress(
                name="Helen Zoe",
                street="47 Eden Street",
                city="Cambridge",
                postcode="CB1 1JR"
            ),
            type="{http://www.example.com/add}UKAddress"
        ),
    ],
    customer_comment_or_ship_comment_or_comment=DerivedElement(
        qname="{http://www.example.com/IPO}comment",
        value="I love Boeing too!",
        type=None
    ),
    items=ItemsType(
        content=[
            ItemsType.Item(
                product_name="777 Model",
                quantity=1,
                usprice=Decimal("99.95"),
                customer_comment_or_ship_comment_or_comment=[],
                ship_date=XmlDate(1999, 12, 5),
                part_num="777-AB",
                weight_kg=Decimal("4.5"),
                ship_by=ItemShipBy.AIR
            ),
        ]
    ),
    order_date=XmlDate(2002, 10, 20)
)
