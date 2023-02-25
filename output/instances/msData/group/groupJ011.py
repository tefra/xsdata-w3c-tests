from output.models.ms_data.group.group_j011_xsd.group_j011 import Doc
from output.models.ms_data.group.group_j011_xsd.group_j011 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        choice=[
            AnyElement(
                qname="b4",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
