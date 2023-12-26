from output.models.saxon_data.open.open001_xsd.open001 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a='',
    b='',
    c='',
    open_com_element=AnyElement(
        children=[
            AnyElement(
                qname='{http://open.com/}extra',
                text='42'
            ),
            AnyElement(
                qname='{http://open.com/}extra',
                text='97'
            ),
        ]
    )
)
