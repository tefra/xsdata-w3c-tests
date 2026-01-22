from output.models.saxon_data.cta.cta0040_xsd.cta0040 import Appendix
from output.models.saxon_data.cta.cta0040_xsd.cta0040 import Chap
from output.models.saxon_data.cta.cta0040_xsd.cta0040 import Doc
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlTime


obj = Doc(
    appendix_or_chap=[
        Chap(
            value=XmlDate(2010, 12, 12),
            type_value='date'
        ),
        Chap(
            value=XmlDateTime(2010, 10, 10, 12, 30, 0),
            type_value='dateTime'
        ),
        Chap(
            value=XmlTime(12, 30, 15, 0, 0),
            type_value='time'
        ),
        Appendix(
            value=XmlDate(2010, 12, 12),
            type_value='date'
        ),
        Appendix(
            value=XmlDateTime(2010, 10, 10, 12, 30, 0, 0, -300),
            type_value='dateTime'
        ),
        Appendix(
            value=XmlTime(12, 30, 15, 0, 0),
            type_value='time'
        ),
    ]
)
