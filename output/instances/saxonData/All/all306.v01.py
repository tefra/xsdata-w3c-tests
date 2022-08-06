from output.models.saxon_data.all.all306_xsd.all306 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        AnyElement(
            qname="b",
            text="",
            tail="text",
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="a",
            text="",
            tail="text",
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="d",
            text="",
            tail="text",
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="a",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
