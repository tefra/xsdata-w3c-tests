from output.models.saxon_data.open.open028_xsd.open028 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a=[
        '',
    ],
    b='',
    c='',
    open_com_element=AnyElement(
        qname='{http://open.com/}extra',
        text='42'
    )
)
