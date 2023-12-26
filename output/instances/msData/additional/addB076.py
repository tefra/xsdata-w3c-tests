from output.models.ms_data.additional.add_b076_xsd.add_b076 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=AnyElement(
        qname='{ns-b}abc',
        text=''
    )
)
