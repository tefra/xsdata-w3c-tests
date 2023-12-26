from decimal import Decimal
from output.models.saxon_data.cta.cta0006_xsd.cta0006 import Message
from output.models.saxon_data.cta.cta0006_xsd.cta0006 import Messages
from xml.etree.ElementTree import QName
from xsdata.models.datatype import XmlDate


obj = Messages(
    message=[
        Message(
            kind=QName("{http://www.w3.org/2001/XMLSchema}int"),
            value=12
        ),
        Message(
            kind=QName("{http://www.w3.org/2001/XMLSchema}date"),
            value=XmlDate(2007, 12, 31)
        ),
        Message(
            kind=QName("{http://www.w3.org/2001/XMLSchema}decimal"),
            value=Decimal('93.7')
        ),
        Message(
            kind=QName("{http://www.w3.org/2001/XMLSchema}QName"),
            value=QName("{http://saxon.sf.net/}assign")
        ),
    ]
)
