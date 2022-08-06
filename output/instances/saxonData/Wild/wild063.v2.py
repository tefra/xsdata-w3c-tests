from output.models.saxon_data.wild.wild063_xsd.wild063 import Doc
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    e=-12,
    f=42,
    local_element=DerivedElement(
        qname="f",
        value=3,
        type=None
    )
)
