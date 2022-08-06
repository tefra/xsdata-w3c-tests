from output.models.saxon_data.cta.cta0023_xsd.cta0023 import Doc
from output.models.saxon_data.cta.cta0023_xsd.cta0023 import Event
from xsdata.models.datatype import XmlDate


obj = Doc(
    event=[
        Event(
            when=XmlDate(2010, 10, 16),
            type="date"
        ),
    ],
    type=None
)
