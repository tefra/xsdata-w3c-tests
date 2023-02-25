from decimal import Decimal
from output.models.ibm_data.mixed.assertions.po_sample.po_xsd.po import Address
from output.models.ibm_data.mixed.assertions.po_sample.po_xsd.po import Buyer
from output.models.ibm_data.mixed.assertions.po_sample.po_xsd.po import Order
from output.models.ibm_data.mixed.assertions.po_sample.po_xsd.product import LongItemDefn
from output.models.ibm_data.mixed.assertions.po_sample.po_xsd.product import Poitems
from output.models.ibm_data.mixed.assertions.po_sample.po_xsd.product import ShortItemDefn
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Order(
    buyer=Buyer(
        choice=[
            "Jimmy",
            DerivedElement(
                qname="lName",
                value="Nice",
                type=None
            ),
        ]
    ),
    billing_address=Address(
        street1="XYZ Street1",
        street2="Near Leapord Market",
        city="ABC",
        zipcode="122001",
        state="PQR",
        country="my country"
    ),
    shipping_address=Address(
        street1=None,
        street2=None,
        city=None,
        zipcode=None,
        state=None,
        country=None
    ),
    email="jimmy.nice@jimmy.org",
    items=Poitems(
        item=[
            LongItemDefn(
                quantity=1,
                price=Decimal("88.10"),
                description="Inside Java Virtual Machine: Sun Press (James Gosling)"
            ),
            ShortItemDefn(
                quantity=2,
                price=Decimal("20"),
                id="105"
            ),
        ]
    ),
    tax=Decimal("10.81"),
    bill_amount=Decimal("118.91"),
    currency="USD",
    id="100"
)
