from output.models.ms_data.schema.sch_d10_a_xsd.sch_d10_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}e1",
            text="",
            children=[
                AnyElement(
                    qname="c21",
                    text="1"
                ),
            ]
        ),
    ]
)
