from output.models.ms_data.group.group_f021_xsd.group_f021 import Doc
from output.models.ms_data.group.group_f021_xsd.group_f021 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        x="",
        a1_or_a2=[
            AnyElement(
                qname="A1",
                text=""
            ),
            AnyElement(
                qname="A2",
                text=""
            ),
            AnyElement(
                qname="A1",
                text=""
            ),
        ]
    )
)
