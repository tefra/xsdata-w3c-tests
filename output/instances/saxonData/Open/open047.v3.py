from output.models.saxon_data.open.open047_xsd.open047 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a=[
        "",
    ],
    b=23,
    d="",
    any_element=AnyElement(
        children=[
            AnyElement(
                qname="x",
                text=""
            ),
            AnyElement(
                qname="b",
                text="not-a-number"
            ),
        ]
    )
)
