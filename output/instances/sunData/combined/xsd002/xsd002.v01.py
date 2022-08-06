from output.models.sun_data.combined.xsd002.xsd002_xsd.xsd002 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    foo_or_bar_or_zot=[
        AnyElement(
            qname="foo",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="this",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="contents",
                    text="",
                    tail="&#10;&#9;&#9;should not be&#10;&#9;&#9;validated&#10;&#9;&#9;",
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="because",
                    text="",
                    tail=None,
                    children=[],
                    attributes={
                        "it": "is ur-type",
                    }
                ),
            ],
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
            text="&#10;&#9;&#9;when using ",
            tail=None,
            children=[
                AnyElement(
                    qname="ur",
                    text="",
                    tail=None,
                    children=[
                        AnyElement(
                            qname="type",
                            text="",
                            tail=None,
                            children=[],
                            attributes={}
                        ),
                    ],
                    attributes={}
                ),
            ],
            attributes={
                "attributes": "are",
                "also": "ignored",
            }
        ),
    ]
)
