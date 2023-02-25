from output.models.ms_data.group.group_e004_xsd.group_e004 import Doc
from output.models.ms_data.group.group_e004_xsd.group_e004 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        x="",
        a1_or_a2=[
            AnyElement(
                qname="A2",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
