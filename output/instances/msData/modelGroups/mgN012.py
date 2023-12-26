from output.models.ms_data.model_groups.mg_n012_xsd.mg_n012 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1='',
    e2='',
    f1='',
    f2='',
    c1_or_c2=AnyElement(
        qname='c1',
        text=''
    ),
    d1_or_d2=AnyElement(
        qname='d1',
        text=''
    )
)
