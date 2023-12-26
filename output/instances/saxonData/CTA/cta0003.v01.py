from decimal import Decimal
from output.models.saxon_data.cta.cta0003_xsd.cta0003 import Message
from output.models.saxon_data.cta.cta0003_xsd.cta0003 import Messages
from output.models.saxon_data.cta.cta0003_xsd.cta0003 import TMin


obj = Messages(
    message=[
        Message(
            e=[
                Decimal('1'),
                Decimal('2'),
                Decimal('3'),
            ],
            min=TMin.VALUE_0
        ),
        Message(
            e=[
                Decimal('1'),
                Decimal('2'),
                Decimal('3'),
            ],
            min=TMin.VALUE_1
        ),
    ]
)
