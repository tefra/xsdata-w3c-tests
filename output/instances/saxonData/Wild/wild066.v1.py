from output.models.saxon_data.wild.wild066_xsd.wild066 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.datatype import XmlTime


obj = Doc(
    e=XmlTime(12, 12, 0, 0),
    f=42,
    local_element=AnyElement(
        qname="e",
        text="2008-11-02",
        tail=None,
        children=[],
        attributes={}
    )
)
