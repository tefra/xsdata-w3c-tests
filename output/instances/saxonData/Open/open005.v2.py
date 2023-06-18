from output.models.saxon_data.open.open006_xsd.open006 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    open_com_element=AnyElement(
        children=[
            AnyElement(
                qname="{http://open.com/}extra",
                text="42"
            ),
            AnyElement(
                qname="{http://open.com/}extra",
                text="43"
            ),
            AnyElement(
                qname="{http://open.com/}extra",
                text="44"
            ),
            AnyElement(
                qname="{http://open.com/}extra",
                text="45"
            ),
            AnyElement(
                qname="{http://open.com/}extra",
                text="46"
            ),
            AnyElement(
                qname="{http://open.com/}extra",
                text="47"
            ),
        ]
    ),
    a="",
    b="",
    c=""
)
