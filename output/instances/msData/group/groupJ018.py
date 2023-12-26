from output.models.ms_data.group.group_j018_xsd.group_j018 import Doc
from output.models.ms_data.group.group_j018_xsd.group_j018 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        b1_or_b2=[
            AnyElement(
                qname='b2',
                text=''
            ),
            AnyElement(
                qname='b2',
                text=''
            ),
        ]
    )
)
