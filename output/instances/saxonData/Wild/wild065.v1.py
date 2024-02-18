from decimal import Decimal
from output.models.saxon_data.wild.wild065_xsd.wild065 import Doc
from output.models.saxon_data.wild.wild065_xsd.wild065 import E
from output.models.saxon_data.wild.wild065_xsd.wild065 import G


obj = Doc(
    g_or_e=E(
        value=Decimal('-12')
    ),
    f=42,
    local_element=G(
        value=6
    )
)
