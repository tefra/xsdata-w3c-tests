from output.models.ms_data.model_groups.mg_f019_xsd.mg_f019 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    any_element=[
        AnyElement(
            qname='{http://n1}foo',
            text=''
        ),
        AnyElement(
            qname='{http://n2}foo',
            text=''
        ),
        AnyElement(
            qname='{http://n3}foo',
            text=''
        ),
        AnyElement(
            qname='{http://n4}foo',
            text=''
        ),
    ],
    e1='',
    e2='',
    e3='',
    e4=''
)
