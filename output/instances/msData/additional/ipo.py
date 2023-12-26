from decimal import Decimal
from output.models.ms_data.additional.ipo_xsd.ipo import Items
from output.models.ms_data.additional.ipo_xsd.ipo import PurchaseOrder
from output.models.ms_data.additional.ipo_xsd.ipo_address import Ukaddress
from output.models.ms_data.additional.ipo_xsd.ipo_address import Usaddress
from output.models.ms_data.additional.ipo_xsd.ipo_address import Usstate
from xsdata.models.datatype import XmlDate


obj = PurchaseOrder(
    ship_to=Ukaddress(
        name='Helen Zoe',
        street='47 Eden Street',
        city='Cambridge',
        postcode='CB1 1JR'
    ),
    bill_to=Usaddress(
        name='Robert Smith',
        street='8 Oak Avenue',
        city='Old Town',
        state=Usstate.PA,
        zip=95819
    ),
    items=Items(
        item=[
            Items.Item(
                product_name='Lapis necklace',
                quantity=1,
                usprice=Decimal('99.95'),
                comment='Want this for the holidays!',
                ship_date=XmlDate(1999, 12, 5),
                part_num='833-AA'
            ),
        ]
    ),
    order_date=XmlDate(1999, 12, 1)
)
