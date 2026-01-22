from output.models.saxon_data.cta.cta0028_xsd.cta0028 import Doc
from output.models.saxon_data.cta.cta0028_xsd.cta0028 import Event
from output.models.saxon_data.cta.cta0028_xsd.cta0028 import When
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
