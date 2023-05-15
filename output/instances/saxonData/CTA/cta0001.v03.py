from output.models.saxon_data.cta.cta0001_xsd.cta0001 import Message
from output.models.saxon_data.cta.cta0001_xsd.cta0001 import MessageTypeValue
from output.models.saxon_data.cta.cta0001_xsd.cta0001 import Messages


obj = Messages(
    message=[
        Message(
            kind=MessageTypeValue.TIME,
            content=[
                "23:59:59",
            ]
        ),
        Message(
            kind=MessageTypeValue.TIME,
            content=[
                "12:00:00",
            ]
        ),
        Message(
            kind=MessageTypeValue.DATE,
            content=[
                "2008-03-01",
            ]
        ),
        Message(
            kind=MessageTypeValue.DATE,
            content=[
                "2008-02-29",
            ]
        ),
        Message(
            content=[
                "bananas and custard",
            ]
        ),
    ]
)
