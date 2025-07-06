from output.models.saxon_data.cta.cta0015_xsd.cta0015 import Doc
from output.models.saxon_data.cta.cta0015_xsd.cta0015 import Event
from output.models.saxon_data.cta.cta0015_xsd.cta0015 import When
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime


obj = Doc(
    event=[
        Event(
            when=When(
                value=XmlDate(2010, 10, 16)
            ),
            type_value='date'
        ),
        Event(
            when=When(
                value=XmlTime(12, 12, 12, 0)
            ),
            type_value='time'
        ),
        Event(
            when=When(
                value=XmlDateTime(2010, 10, 16, 13, 13, 0)
            ),
            type_value='dateTime'
        ),
        Event(
            when=When(
                value=XmlPeriod("2010-10")
            )
        ),
    ]
)
