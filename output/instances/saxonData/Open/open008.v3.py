from output.models.saxon_data.open.open008_xsd.open008 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    open_com_element=AnyElement(
        qname=None,
        text=None,
        tail=None,
        children=[
            AnyElement(
                qname="{http://open.com/}extra",
                text="42",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="{http://open.com/}extra",
                text="42",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="{http://open.com/}extra",
                text="42",
                tail=None,
                children=[],
                attributes={}
            ),
        ],
        attributes={}
    ),
    a=[
        "",
        "",
    ],
    b="",
    c=""
)