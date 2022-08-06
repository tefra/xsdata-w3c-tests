from output.models.ms_data.schema.sch_q1_a_xsd.sch_q1_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}e1",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="{ns-a}b1",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="{ns-a}b3",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            attributes={}
        ),
        AnyElement(
            qname="{ns-a}b-e1",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="{ns-a}b2",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="{ns-a}b4",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            attributes={}
        ),
    ]
)
