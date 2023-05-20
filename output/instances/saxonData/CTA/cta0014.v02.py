from output.models.saxon_data.cta.cta0014_xsd.cta0014 import Doc
from output.models.saxon_data.cta.cta0014_xsd.cta0014 import Event
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime


obj = Doc(
    event=[
        Event(
            when=XmlDate(2010, 10, 16),
            type="date"
        ),
        Event(
            when=XmlTime(12, 12, 12, 0),
            type="time"
        ),
        Event(
            when=XmlDateTime(2010, 10, 16, 13, 13, 0),
            type="dateTime"
        ),
        Event(
            when=XmlPeriod("2010-10"),
            type="other"
        ),
    ]
)
