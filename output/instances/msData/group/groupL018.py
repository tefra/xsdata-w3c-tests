from output.models.ms_data.group.group_l018_xsd.group_l018 import Doc
from output.models.ms_data.group.group_l018_xsd.group_l018 import Elem
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
