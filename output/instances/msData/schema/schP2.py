from output.models.ms_data.schema.sch_p2_a_xsd.sch_p2_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}e1",
            text="1234"
        ),
        AnyElement(
            qname="{ns-a}b-e1",
            text="abcd"
        ),
    ]
)
