from output.models.ms_data.model_groups.mg_h014_xsd.mg_h014 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=AnyElement(
        qname="e2",
        text=""
    )
)
