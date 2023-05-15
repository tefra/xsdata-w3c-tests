from output.models.ms_data.schema.sch_g1_a_xsd.sch_g1_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}e1",
            text="",
            children=[
                AnyElement(
                    qname="a1",
                    text="123"
                ),
                AnyElement(
                    qname="a2",
                    text="true"
                ),
            ]
        ),
        AnyElement(
            qname="{ns-b}e1",
            text="",
            children=[
                AnyElement(
                    qname="a1",
                    text="true"
                ),
                AnyElement(
                    qname="a2",
                    text="123"
                ),
            ]
        ),
        AnyElement(
            qname="{ns-c}e1",
            text="",
            children=[
                AnyElement(
                    qname="a1",
                    text="123"
                ),
                AnyElement(
                    qname="a2",
                    text="123"
                ),
            ]
        ),
    ]
)
