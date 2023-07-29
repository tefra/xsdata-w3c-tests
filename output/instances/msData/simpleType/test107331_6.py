from decimal import Decimal
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Item
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Root
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlHexBinary
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime


obj = Root(
    choice=[
        Item(
            value="abc"
        ),
        DerivedElement(
            qname="item",
            value=123
        ),
        DerivedElement(
            qname="item",
            value=4.56
        ),
        DerivedElement(
            qname="item",
            value="this is a string"
        ),
        DerivedElement(
            qname="item",
            value=False
        ),
        DerivedElement(
            qname="item",
            value=Decimal("45")
        ),
        DerivedElement(
            qname="item",
            value=XmlDuration("P1347Y")
        ),
        DerivedElement(
            qname="item",
            value=XmlDateTime(1999, 5, 31, 13, 20, 0, 0, -300)
        ),
        DerivedElement(
            qname="item",
            value=XmlTime(13, 20, 0, 0, -300)
        ),
        DerivedElement(
            qname="item",
            value=XmlDate(1999, 5, 31)
        ),
        DerivedElement(
            qname="item",
            value=XmlPeriod("1999")
        ),
        DerivedElement(
            qname="item",
            value=XmlPeriod("--02-13")
        ),
        DerivedElement(
            qname="item",
            value=b"\xab\xcd"
        ),
        DerivedElement(
            qname="item",
            value="http://tempuri"
        ),
        DerivedElement(
            qname="item",
            value="123"
        ),
    ]
)
