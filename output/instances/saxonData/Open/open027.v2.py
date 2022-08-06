from output.models.saxon_data.open.open027_xsd.open027 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a=[
        "",
    ],
    b="",
    c="",
    d="",
    open_com_element=AnyElement(
        qname="{http://open.com/}extra",
        text="42",
        tail=None,
        children=[],
        attributes={}
    )
)
