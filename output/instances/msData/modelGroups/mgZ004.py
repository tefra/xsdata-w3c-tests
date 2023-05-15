from output.models.ms_data.model_groups.mg_z004_xsd.mg_z004 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    content=[
        AnyElement(
            qname="{urn:test}A",
            text=""
        ),
    ]
)
