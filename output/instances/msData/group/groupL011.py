from output.models.ms_data.group.group_l011_xsd.group_l011 import Doc
from output.models.ms_data.group.group_l011_xsd.group_l011 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        b1_or_b2=[
            AnyElement(
                qname="b1",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
