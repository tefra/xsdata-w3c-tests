from output.models.saxon_data.open.open031_xsd.open031 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    open_com_element=AnyElement(
        qname='{http://open.com/}extra',
        text='42'
    ),
    a=[
        '',
    ],
    b='',
    c='',
    d=''
)
