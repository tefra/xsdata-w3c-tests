from output.models.ms_data.schema.sch_q3_a_xsd.sch_q3_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}e1",
            text="",
            children=[
                AnyElement(
                    qname="{ns-a}b1",
                    text=""
                ),
            ]
        ),
        AnyElement(
            qname="{ns-a}b-e1",
            text="",
            children=[
                AnyElement(
                    qname="{ns-a}b2",
                    text=""
                ),
            ]
        ),
    ]
)
