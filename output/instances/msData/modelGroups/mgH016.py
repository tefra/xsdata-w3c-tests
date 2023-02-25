from output.models.ms_data.model_groups.mg_h016_xsd.mg_h016 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=[
        AnyElement(
            qname="e1",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
