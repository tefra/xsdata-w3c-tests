from output.models.saxon_data.open.open022_xsd.open022 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    open_com_element=[
        AnyElement(
            qname="{http://open.com/}extra",
            text="42",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://open.com/}extra",
            text="97",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
