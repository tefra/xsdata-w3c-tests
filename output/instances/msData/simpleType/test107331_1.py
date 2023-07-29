from decimal import Decimal
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Item
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Root
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime


obj = Root(
    choice=[
        Item(
            value="abc"
        ),
        123,
        -123,
        DerivedElement(
            qname="string",
            value="this is a string"
        ),
        True,
        False,
        DerivedElement(
            qname="float",
            value=1.2
        ),
        DerivedElement(
            qname="float",
            value=5.24276
        ),
        DerivedElement(
            qname="float",
            value=5.24276
        ),
        Decimal("56"),
        Decimal("-56"),
        Decimal("-562135"),
        XmlDuration("P1347Y"),
        XmlDateTime(1999, 5, 31, 13, 20, 0, 0, -300),
        XmlTime(13, 20, 0, 0, -300),
        XmlDate(1999, 5, 31),
        DerivedElement(
            qname="year",
            value=XmlPeriod("2004")
        ),
        DerivedElement(
            qname="monthday",
            value=XmlPeriod("--02-13")
        ),
        DerivedElement(
            qname="day",
            value=XmlPeriod("---15")
        ),
        XmlPeriod("--12"),
        b"\xab\xcd",
        DerivedElement(
            qname="anyuri",
            value="http://tempuri"
        ),
    ]
)
