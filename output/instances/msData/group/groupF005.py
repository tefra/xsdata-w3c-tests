from output.models.ms_data.group.group_f005_xsd.group_f005 import Doc
from output.models.ms_data.group.group_f005_xsd.group_f005 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        x="",
        a1_or_a2=[
            AnyElement(
                qname="A1",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
