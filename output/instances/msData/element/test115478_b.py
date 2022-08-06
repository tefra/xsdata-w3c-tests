from output.models.ms_data.element.test115478_b_xsd.test115478_b import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    local_element=AnyElement(
        qname="e",
        text="123",
        tail=None,
        children=[],
        attributes={}
    )
)
