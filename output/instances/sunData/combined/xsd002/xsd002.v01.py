from output.models.sun_data.combined.xsd002.xsd002_xsd.xsd002 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    foo_or_bar_or_zot=[
        AnyElement(
            qname="foo",
            text="",
            children=[
                AnyElement(
                    qname="this",
                    text=""
                ),
                AnyElement(
                    qname="contents",
                    text="",
                    tail="&#10;&#9;&#9;should not be&#10;&#9;&#9;validated&#10;&#9;&#9;"
                ),
                AnyElement(
                    qname="because",
                    text="",
                    attributes={
                        "it": "is ur-type",
                    }
                ),
            ]
        ),
        AnyElement(
            qname="{http://foo.com}bar",
            text=""
        ),
        AnyElement(
            qname="zot",
            text="&#10;&#9;&#9;when using ",
            children=[
                AnyElement(
                    qname="ur",
                    text="",
                    children=[
                        AnyElement(
                            qname="type",
                            text=""
                        ),
                    ]
                ),
            ],
            attributes={
                "attributes": "are",
                "also": "ignored",
            }
        ),
    ]
)
