from output.models.ms_data.model_groups.mg_i016_xsd.mg_i016 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    choice=AnyElement(
        qname="c3",
        text=""
    )
)
