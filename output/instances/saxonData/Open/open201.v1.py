from decimal import Decimal
from output.models.saxon_data.open.open201_xsd.open201 import AType
from output.models.saxon_data.open.open201_xsd.open201 import Doc
from xsdata.models.datatype import XmlDate


obj = Doc(
    extra_number=Decimal("1.234"),
    extra_date=XmlDate(2008, 3, 12),
    a=AType(
        extra_number=Decimal("1.456"),
        extra_date=None
    ),
    b=None,
    c=None
)
