from decimal import Decimal
from output.models.saxon_data.open.open205_xsd.open205 import AType
from output.models.saxon_data.open.open205_xsd.open205 import Doc
from output.models.saxon_data.open.open205_xsd.open205x import BType
from xsdata.models.datatype import XmlDate


obj = Doc(
    a=AType(
        extra_number=Decimal('23.45'),
        extra_date=XmlDate(2007, 12, 12)
    ),
    b=BType(

    )
)
