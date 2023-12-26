from output.models.ms_data.model_groups.mg_l006_xsd.mg_l006 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=AnyElement(
        qname='e1',
        text=''
    )
)
