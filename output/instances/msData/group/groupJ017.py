from output.models.ms_data.group.group_j017_xsd.group_j017 import Doc
from output.models.ms_data.group.group_j017_xsd.group_j017 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        b1_or_b2=[
            AnyElement(
                qname="b2",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
