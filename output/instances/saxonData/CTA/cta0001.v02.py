from output.models.saxon_data.cta.cta0001_xsd.cta0001 import Message
from output.models.saxon_data.cta.cta0001_xsd.cta0001 import MessageTypeValue


obj = Message(
    kind=MessageTypeValue.TIME,
    content=[
        "23:59:59",
    ]
)
