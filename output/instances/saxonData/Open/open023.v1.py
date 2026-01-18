from output.models.saxon_data.open.open024_xsd.open024 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a='',
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
