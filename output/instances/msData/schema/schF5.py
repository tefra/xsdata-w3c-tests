from output.models.ms_data.schema.sch_f5_a_xsd.sch_f5_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}e1",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="a1",
                    text="123",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="a2",
                    text="true",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            attributes={}
        ),
        AnyElement(
            qname="{ns-b}e1",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="a1",
                    text="true",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="a2",
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
