from output.models.ms_data.group.group_n017_xsd.group_n017 import Doc
from output.models.ms_data.group.group_n017_xsd.group_n017 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        a1_or_a2=[
            AnyElement(
                qname='a2',
                text=''
            ),
        ]
    )
)
