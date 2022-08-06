from decimal import Decimal
from output.models.ms_data.additional.po_xsd.po import Items
from output.models.ms_data.additional.po_xsd.po import PurchaseOrder
from output.models.ms_data.additional.po_xsd.po import Usaddress
from xsdata.models.datatype import XmlDate


obj = PurchaseOrder(
    ship_to=Usaddress(
        name="Alice Smith",
        street="123 Maple Street",
        city="Mill Valley",
        state="CA",
        zip=Decimal("90952"),
        country="US"
    ),
    bill_to=Usaddress(
        name="Robert Smith",
        street="8 Oak Avenue",
        city="Old Town",
        state="PA",
        zip=Decimal("95819"),
        country="US"
    ),
    comment="Hurry, my lawn is going wild!",
    items=Items(
        item=[
            Items.Item(
                product_name="Lawnmower",
                quantity=1,
                usprice=Decimal("148.95"),
                comment="Confirm this is electric",
                ship_date=None,
                part_num="872-AA"
            ),
            Items.Item(
                product_name="Baby Monitor",
                quantity=1,
                usprice=Decimal("39.98"),
                comment=None,
                ship_date=XmlDate(1999, 5, 21),
                part_num="926-AA"
            ),
        ]
    ),
    order_date=XmlDate(1999, 10, 20)
)
