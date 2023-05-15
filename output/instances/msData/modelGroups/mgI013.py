from output.models.ms_data.model_groups.mg_i013_xsd.mg_i013 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    choice=[
        AnyElement(
            qname="d",
            text=""
        ),
    ]
)
