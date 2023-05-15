from decimal import Decimal
from output.models.saxon_data.wild.wild065_xsd.wild065 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    g_or_e=Decimal("-12"),
    f=42,
    local_element=AnyElement(
        qname="g",
        text="6"
    )
)
