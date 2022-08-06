from decimal import Decimal
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Root
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlHexBinary
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime


obj = Root(
    entity=[],
    anyuri=[],
    hexbinary=[],
    month=[],
    day=[],
    monthday=[],
    year=[],
    date=[],
    time=[],
    datetime=[],
    duration=[],
    decimal=[],
    double=[],
    float_value=[],
    bool_value=[],
    int_value=[],
    string=[],
    item=[
        "abc",
        123,
        4.56,
        "this is a string",
        False,
        Decimal("45"),
        XmlDuration("P1347Y"),
        XmlDateTime(1999, 5, 31, 13, 20, 0, 0, -300),
        XmlTime(13, 20, 0, 0, -300),
        XmlDate(1999, 5, 31),
        XmlPeriod("1999"),
        XmlPeriod("--02-13"),
        b"\xab\xcd",
        "http://tempuri",
        "123",
    ]
)
