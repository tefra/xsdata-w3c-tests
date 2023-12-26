from output.models.ms_data.group.group_h002_xsd.group_h002 import Doc
from output.models.ms_data.group.group_h002_xsd.group_h002 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        choice=[
            AnyElement(
                qname='x1',
                text=''
            ),
            AnyElement(
                qname='x2',
                text=''
            ),
        ]
    )
)
