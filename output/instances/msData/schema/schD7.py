from output.models.ms_data.schema.sch_d7_a_xsd.ns_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}e1",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="{ns-a}a1",
                    text="123",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="{ns-a}a2",
                    text="true",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            attributes={}
        ),
        AnyElement(
            qname="{ns-a}e3",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="c1",
                    text="123",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="c2",
                    text="123",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            attributes={}
        ),
    ]
)
