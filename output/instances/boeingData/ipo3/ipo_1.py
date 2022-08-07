from decimal import Decimal
from output.models.boeing_data.ipo3.ipo_xsd.address import Usaddress
from output.models.boeing_data.ipo3.ipo_xsd.address import Usstate
from output.models.boeing_data.ipo3.ipo_xsd.ipo import ItemsType
from output.models.boeing_data.ipo3.ipo_xsd.ipo import PurchaseOrder
from output.models.boeing_data.ipo3.ipo_xsd.itematt import ItemDeliveryShipBy
from xsdata.models.datatype import XmlDate


obj = PurchaseOrder(
    ship_to=Usaddress(
        name="Alice Smith",
        street="123 Maple Street",
        city="Mill Valley",
        state=Usstate.CA,
        zip=90952
    ),
    bill_to=Usaddress(
        name="Robert Smith",
        street="8 Oak Avenue",
        city="Old Town",
        state=Usstate.PA,
        zip=95819
    ),
    single_address=None,
    customer_comment=None,
    ship_comment="Hurry, my sister loves Boeing!",
    comment=None,
    items=ItemsType(
        content=[
            ItemsType.Item(
                product_name="777 Model",
                quantity=1,
                usprice=Decimal("99.95"),
                customer_comment=[
                    " Want this for the holidays! ",
                ],
                ship_comment=[
                    " Use gold wrap if possible ",
                ],
                comment=[],
                ship_date=XmlDate(1999, 12, 5),
                part_num="777-BA",
                weight_kg=Decimal("4.5"),
                ship_by=ItemDeliveryShipBy.AIR
            ),
            ItemsType.Item(
                product_name="833 Model",
                quantity=2,
                usprice=Decimal("199.95"),
                customer_comment=[],
                ship_comment=[],
                comment=[],
                ship_date=XmlDate(2000, 2, 28),
                part_num="833-AA",
                weight_kg=None,
                ship_by=None
            ),
        ]
    ),
    order_date=XmlDate(2002, 10, 20)
)
