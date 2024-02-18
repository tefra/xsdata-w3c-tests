from decimal import Decimal
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Anyuri
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Bool
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Date
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Datetime
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Day
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import DecimalType
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Duration
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Float
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Hexbinary
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Int
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Item
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Month
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Monthday
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Root
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import String
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Time
from output.models.ms_data.simple_type.test107331_a_xsd.test107331_a import Year
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime


obj = Root(
    choice=[
        Item(
            value='abc'
        ),
        Int(
            value=123
        ),
        Int(
            value=-123
        ),
        String(
            value='this is a string'
        ),
        Bool(
            value=True
        ),
        Bool(
            value=False
        ),
        Float(
            value=1.2
        ),
        Float(
            value=5.24276
        ),
        Float(
            value=5.24276
        ),
        DecimalType(
            value=Decimal('56')
        ),
        DecimalType(
            value=Decimal('-56')
        ),
        DecimalType(
            value=Decimal('-562135')
        ),
        Duration(
            value=XmlDuration("P1347Y")
        ),
        Datetime(
            value=XmlDateTime(1999, 5, 31, 13, 20, 0, 0, -300)
        ),
        Time(
            value=XmlTime(13, 20, 0, 0, -300)
        ),
        Date(
            value=XmlDate(1999, 5, 31)
        ),
        Year(
            value=XmlPeriod("2004")
        ),
        Monthday(
            value=XmlPeriod("--02-13")
        ),
        Day(
            value=XmlPeriod("---15")
        ),
        Month(
            value=XmlPeriod("--12")
        ),
        Hexbinary(
            value=b'\xab\xcd'
        ),
        Anyuri(
            value='http://tempuri'
        ),
    ]
)
