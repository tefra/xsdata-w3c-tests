from output.models.ms_data.schema.sch_t10_a_xsd.sch_t10_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}b-e1",
            text="",
            attributes={
                "att1": "123",
                "att2": "bar",
            }
        ),
        AnyElement(
            qname="{ns-a}e2",
            text="12"
        ),
    ]
)
