from output.models.ms_data.group.group_n018_xsd.group_n018 import Doc
from output.models.ms_data.group.group_n018_xsd.group_n018 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        a1_or_a2=[
            AnyElement(
                qname="a2",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="a1",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
