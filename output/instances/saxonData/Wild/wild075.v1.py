from output.models.saxon_data.wild.wild075_xsd.wild075 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a=23,
    local_element=AnyElement(
        qname="b",
        text="2010-10-16",
        tail=None,
        children=[],
        attributes={}
    )
)
