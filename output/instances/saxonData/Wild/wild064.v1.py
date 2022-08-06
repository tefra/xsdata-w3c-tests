from output.models.saxon_data.wild.wild064_xsd.wild064 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e=-12,
    f=42,
    local_element=AnyElement(
        qname="g",
        text="6",
        tail=None,
        children=[],
        attributes={}
    )
)
