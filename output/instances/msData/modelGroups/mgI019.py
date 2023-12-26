from output.models.ms_data.model_groups.mg_i019_xsd.mg_i019 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    choice=AnyElement(
        qname='e2',
        text=''
    )
)
