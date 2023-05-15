from output.models.saxon_data.wild.wild064_xsd.wild064 import Doc
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    e=-12,
    f=42,
    local_element=DerivedElement(
        qname="e",
        value=93
    )
)
