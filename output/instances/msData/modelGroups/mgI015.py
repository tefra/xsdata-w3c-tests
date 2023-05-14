from output.models.ms_data.model_groups.mg_i015_xsd.mg_i015 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    choice=AnyElement(
        qname="four",
        text="",
        tail=None,
        children=[],
        attributes={}
    )
)
