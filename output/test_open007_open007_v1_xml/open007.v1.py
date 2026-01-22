from output.models.saxon_data.open.open007_xsd.open007 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    open_com_element=AnyElement(
        children=[
            AnyElement(
                qname='{http://open.com/}extra',
                text=''
            ),
            AnyElement(
                qname='{http://open.com/}extra',
                text=''
            ),
            AnyElement(
                qname='{http://open.com/}extra',
                text=''
            ),
            AnyElement(
                qname='{http://open.com/}extra',
                text=''
            ),
        ]
    ),
    a=[
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    ]
)
