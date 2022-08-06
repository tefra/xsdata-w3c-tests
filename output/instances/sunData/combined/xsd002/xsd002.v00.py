from output.models.sun_data.combined.xsd002.xsd002_xsd.xsd002 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    foo_or_bar_or_zot=[
        AnyElement(
            qname="foo",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://foo.com}bar",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="zot",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="foo",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://foo.com}bar",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="zot",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
