from output.models.saxon_data.open.open021_xsd.open021 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        "&#10;  o-O-o&#10;  ",
        AnyElement(
            qname="{http://open.com/}extra",
            text="42",
            tail="&#10;  o-O-o  &#10;  "
        ),
        AnyElement(
            qname="{http://open.com/}extra",
            text="97",
            tail=" &#10;  o-O-o   &#10;"
        ),
    ]
)
