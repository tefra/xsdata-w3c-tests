from output.models.saxon_data.cta.cta0001_xsd.cta0001 import Message
from output.models.saxon_data.cta.cta0001_xsd.cta0001 import MessageTypeValue
from output.models.saxon_data.cta.cta0001_xsd.cta0001 import Messages


obj = Messages(
    message=[
        Message(
            kind=MessageTypeValue.TIME,
            any_attributes={},
            content=[
                "23:59:59",
            ]
        ),
        Message(
            kind=MessageTypeValue.TIME,
            any_attributes={},
            content=[
                "12:00:00",
            ]
        ),
        Message(
            kind=MessageTypeValue.DATE,
            any_attributes={},
            content=[
                "2008-03-01",
            ]
        ),
        Message(
            kind=MessageTypeValue.DATE,
            any_attributes={},
            content=[
                "2008-02-29",
            ]
        ),
        Message(
            kind=None,
            any_attributes={},
            content=[
                "bananas and custard",
            ]
        ),
    ]
)
