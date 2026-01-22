from output.models.saxon_data.cta.cta0018_xsd.cta0018 import Doc
from output.models.saxon_data.cta.cta0018_xsd.cta0018 import Event
from output.models.saxon_data.cta.cta0018_xsd.cta0018 import When
from xsdata.models.datatype import XmlDate


obj = Doc(
    event=[
        Event(
            when=When(
                value=XmlDate(2010, 10, 16)
            ),
            type_value='date'
        ),
    ]
)
