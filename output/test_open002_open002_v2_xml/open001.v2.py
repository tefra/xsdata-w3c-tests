from output.models.saxon_data.open.open002_xsd.open002 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a='',
    b='',
    open_com_element=AnyElement(
        qname='{http://open.com/}extra',
        text='42'
    )
)
