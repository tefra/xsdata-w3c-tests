from output.models.saxon_data.cta.cta0017_xsd.cta0017 import Doc
from output.models.saxon_data.cta.cta0017_xsd.cta0017 import Event
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