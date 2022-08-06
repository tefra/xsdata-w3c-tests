from decimal import Decimal
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Root
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime


obj = Root(
    entity=[],
    anyuri=[
        "http://tempuri",
    ],
    hexbinary=[
        b"\xab\xcd",
    ],
    month=[
        XmlPeriod("--12"),
    ],
    day=[
        XmlPeriod("---15"),
    ],
    monthday=[
        XmlPeriod("--02-13"),
    ],
    year=[
        XmlPeriod("2004"),
    ],
    date=[
        XmlDate(1999, 5, 31),
    ],
    time=[
        XmlTime(13, 20, 0, 0, -300),
    ],
    datetime=[
        XmlDateTime(1999, 5, 31, 13, 20, 0, 0, -300),
    ],
    duration=[
        XmlDuration("P1347Y"),
    ],
    decimal=[
        Decimal("56"),
        Decimal("-56"),
        Decimal("-562135"),
    ],
    double=[],
    float_value=[
        1.2,
        5.24276,
        5.24276,
    ],
    bool_value=[
        True,
        False,
    ],
    int_value=[
        123,
        -123,
    ],
    string=[
        "this is a string",
    ],
    item=[
        "abc",
    ]
)
