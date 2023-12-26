from output.models.ms_data.group.group_h005_xsd.group_h005 import Doc
from output.models.ms_data.group.group_h005_xsd.group_h005 import Elem
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
