from output.models.ms_data.model_groups.mg_l009_xsd.mg_l009 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    choice=AnyElement(
        qname="e2",
        text="",
        tail=None,
        children=[],
        attributes={}
    )
)
