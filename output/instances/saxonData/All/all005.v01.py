from output.models.saxon_data.all.all005_xsd.all005 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        AnyElement(
            qname="{http://a.ns/}wasp",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://b.ns/}bee",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://a.ns/}ant",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://b.ns/}beetle",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://a.ns/}earwig",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://b.ns/}maybug",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
