from output.models.saxon_data.wild.wild063_xsd.wild063 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e=-12,
    f=42,
    local_element=AnyElement(
        qname="e",
        text="12"
    )
)
