from output.models.saxon_data.wild.wild077_xsd.wild077 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a=23,
    local_element=AnyElement(
        qname="a",
        text="2010-10-16",
        tail=None,
        children=[],
        attributes={}
    )
)
