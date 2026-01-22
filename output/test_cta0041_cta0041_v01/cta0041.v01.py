from output.models.saxon_data.cta.cta0041_xsd.cta0041 import Appendix
from output.models.saxon_data.cta.cta0041_xsd.cta0041 import Chap
from output.models.saxon_data.cta.cta0041_xsd.cta0041 import Doc
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
            value=XmlDateTime(2010, 10, 10, 12, 30, 0, 0, 0),
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
            value=XmlTime(12, 30, 15, 0, 0),
            type_value='time'
        ),
    ]
)
