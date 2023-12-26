from output.models.saxon_data.cta.cta0021_xsd.cta0021 import Doc
from output.models.saxon_data.cta.cta0021_xsd.cta0021 import Event
from xsdata.models.datatype import XmlDate


obj = Doc(
    event=[
        Event(
            when=XmlDate(2010, 10, 16),
            type_value='date'
        ),
    ]
)
