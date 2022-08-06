from decimal import Decimal
from output.models.saxon_data.open.open202_xsd.open202 import AType
from output.models.saxon_data.open.open202_xsd.open202 import Doc
from xsdata.models.datatype import XmlDate


obj = Doc(
    extra_number=Decimal("1.234"),
    extra_date=XmlDate(2008, 3, 12),
    a=AType(

    ),
    b=None,
    c=None
)
