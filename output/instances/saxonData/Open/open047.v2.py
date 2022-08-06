from output.models.saxon_data.open.open047_xsd.open047 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    open_com_element=None,
    a=[
        "",
    ],
    b=23,
    c=None,
    d="",
    any_element=AnyElement(
        qname="{http://closed.com/}x",
        text="",
        tail=None,
        children=[],
        attributes={}
    )
)
