from output.models.saxon_data.open.open013_xsd.open013 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        "&#10;  (",
        AnyElement(
            qname="{http://open.com/}extra",
            text="",
            tail=")&#10;",
            children=[],
            attributes={}
        ),
    ]
)
