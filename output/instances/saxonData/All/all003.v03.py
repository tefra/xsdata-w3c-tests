from output.models.saxon_data.all.all003_xsd.all003 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        AnyElement(
            qname="a",
            text="",
            tail="banana"
        ),
        AnyElement(
            qname="b",
            text="",
            tail="custard"
        ),
        AnyElement(
            qname="c",
            text="",
            tail="mango"
        ),
        AnyElement(
            qname="d",
            text="",
            tail="pineapples and cream"
        ),
    ]
)
