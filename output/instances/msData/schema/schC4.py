from output.models.ms_data.schema.sch_c4_a_xsd.sch_c4_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}e1",
            text="",
            children=[
                AnyElement(
                    qname="{ns-a}a1",
                    text="123"
                ),
                AnyElement(
                    qname="{ns-a}a2",
                    text="true"
                ),
            ]
        ),
        AnyElement(
            qname="{ns-a}e2",
            text="",
            children=[
                AnyElement(
                    qname="{ns-a}b1",
                    text="true"
                ),
                AnyElement(
                    qname="{ns-a}b2",
                    text="123"
                ),
            ]
        ),
    ]
)
