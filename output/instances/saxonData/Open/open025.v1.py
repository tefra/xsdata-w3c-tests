from output.models.saxon_data.open.open025_xsd.open025 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.datatype import XmlDate


obj = Doc(
    local_element=AnyElement(
        children=[
            AnyElement(
                qname="j",
                text="banana"
            ),
            AnyElement(
                qname="a",
                text="17"
            ),
        ]
    ),
    i=[
        12,
        42,
    ],
    d=[
        XmlDate(2008, 8, 8),
    ]
)
