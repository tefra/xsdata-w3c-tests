from output.models.saxon_data.cta.cta0040_xsd.cta0040 import Appendix
from output.models.saxon_data.cta.cta0040_xsd.cta0040 import Chap
from output.models.saxon_data.cta.cta0040_xsd.cta0040 import Doc
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlTime


obj = Doc(
    appendix=[
        Appendix(
            value=XmlDate(2010, 12, 12),
            type="date"
        ),
        Appendix(
            value=XmlDateTime(2010, 10, 10, 12, 30, 0, 0, -300),
            type="dateTime"
        ),
        Appendix(
            value=XmlTime(12, 30, 15, 0, 0),
            type="time"
        ),
    ],
    chap=[
        Chap(
            value=XmlDate(2010, 12, 12),
            type="date"
        ),
        Chap(
            value=XmlDateTime(2010, 10, 10, 12, 30, 0),
            type="dateTime"
        ),
        Chap(
            value=XmlTime(12, 30, 15, 0, 0),
            type="time"
        ),
    ]
)