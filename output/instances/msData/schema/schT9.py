from output.models.ms_data.schema.sch_t9_a_xsd.sch_t9_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}b-e1",
            text="",
            tail=None,
            children=[],
            attributes={
                "att1": "123",
            }
        ),
        AnyElement(
            qname="{ns-a}e2",
            text="12",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
