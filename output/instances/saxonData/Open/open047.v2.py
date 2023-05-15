from output.models.saxon_data.open.open047_xsd.open047 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a=[
        "",
    ],
    b=23,
    d="",
    any_element=AnyElement(
        qname="{http://closed.com/}x",
        text=""
    )
)
