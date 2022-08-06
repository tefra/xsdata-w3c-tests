from output.models.ms_data.schema.sch_g12_a_xsd.sch_g12_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{ns-a}foo_a",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{ns-b}foo_b",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{ns-b}foo_c",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
