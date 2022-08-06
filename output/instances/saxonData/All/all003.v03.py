from output.models.saxon_data.all.all003_xsd.all003 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        AnyElement(
            qname="a",
            text="",
            tail="banana",
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="b",
            text="",
            tail="custard",
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="c",
            text="",
            tail="mango",
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="d",
            text="",
            tail="pineapples and cream",
            children=[],
            attributes={}
        ),
    ]
)
