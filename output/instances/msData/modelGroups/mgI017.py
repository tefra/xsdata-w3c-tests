from output.models.ms_data.model_groups.mg_i017_xsd.mg_i017 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    choice=AnyElement(
        qname='c2',
        text=''
    )
)
