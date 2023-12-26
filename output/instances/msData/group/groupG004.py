from output.models.ms_data.group.group_g004_xsd.group_g004 import Doc
from output.models.ms_data.group.group_g004_xsd.group_g004 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        choice=[
            AnyElement(
                qname='y1',
                text=''
            ),
            AnyElement(
                qname='y2',
                text=''
            ),
        ]
    )
)
