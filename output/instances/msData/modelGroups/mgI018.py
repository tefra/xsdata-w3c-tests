from output.models.ms_data.model_groups.mg_i018_xsd.mg_i018 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    choice=AnyElement(
        qname='{http://n4}foo',
        text=''
    )
)
