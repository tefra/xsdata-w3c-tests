from decimal import Decimal
from output.models.saxon_data.complex.complex006_xsd.complex006 import Root


obj = Root(
    value=Decimal("1234.56"),
    nil="true"
)
