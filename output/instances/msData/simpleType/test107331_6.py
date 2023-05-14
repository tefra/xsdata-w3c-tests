from decimal import Decimal
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlHexBinary
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime


obj = Root(
    choice=[
        AnyElement(
            qname="item",
            text="abc",
            tail=None,
            children=[],
            attributes={}
        ),
        DerivedElement(
            qname="item",
            value=123,
            type=None
        ),
        DerivedElement(
            qname="item",
            value=4.56,
            type=None
        ),
        DerivedElement(
            qname="item",
            value="this is a string",
            type=None
        ),
        DerivedElement(
            qname="item",
            value=False,
            type=None
        ),
        DerivedElement(
            qname="item",
            value=Decimal("45"),
            type=None
        ),
        DerivedElement(
            qname="item",
            value=XmlDuration("P1347Y"),
            type=None
        ),
        DerivedElement(
            qname="item",
            value=XmlDateTime(1999, 5, 31, 13, 20, 0, 0, -300),
            type=None
        ),
        DerivedElement(
            qname="item",
            value=XmlTime(13, 20, 0, 0, -300),
            type=None
        ),
        DerivedElement(
            qname="item",
            value=XmlDate(1999, 5, 31),
            type=None
        ),
        DerivedElement(
            qname="item",
            value=XmlPeriod("1999"),
            type=None
        ),
        DerivedElement(
            qname="item",
            value=XmlPeriod("--02-13"),
            type=None
        ),
        DerivedElement(
            qname="item",
            value=b"\xab\xcd",
            type=None
        ),
        DerivedElement(
            qname="item",
            value="http://tempuri",
            type=None
        ),
        DerivedElement(
            qname="item",
            value="123",
            type=None
        ),
    ]
)
