from output.models.saxon_data.all.all004_xsd.all004 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        AnyElement(
            qname="a",
            text=""
        ),
        AnyElement(
            qname="b",
            text=""
        ),
        AnyElement(
            qname="d",
            text=""
        ),
        AnyElement(
            qname="c",
            text=""
        ),
        AnyElement(
            qname="a",
            text="",
            tail="strawberries&#10;  "
        ),
        AnyElement(
            qname="c",
            text=""
        ),
        AnyElement(
            qname="c",
            text=""
        ),
        AnyElement(
            qname="a",
            text=""
        ),
        AnyElement(
            qname="a",
            text=""
        ),
        AnyElement(
            qname="b",
            text=""
        ),
    ]
)
