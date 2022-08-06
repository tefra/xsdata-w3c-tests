from output.models.saxon_data.open.open025_xsd.open025 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.datatype import XmlDate


obj = Doc(
    local_element=AnyElement(
        qname=None,
        text=None,
        tail=None,
        children=[
            AnyElement(
                qname="j",
                text="banana",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="a",
                text="17",
                tail=None,
                children=[],
                attributes={}
            ),
        ],
        attributes={}
    ),
    i=[
        12,
        42,
    ],
    d=[
        XmlDate(2008, 8, 8),
    ]
)
