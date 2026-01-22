from output.models.saxon_data.open.open047_xsd.open047 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    open_com_element=AnyElement(
        qname='{http://open.com/}x',
        text=''
    ),
    a=[
        '',
    ],
    b=23,
    d=''
)
