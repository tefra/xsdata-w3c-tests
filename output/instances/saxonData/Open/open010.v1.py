from output.models.saxon_data.open.open010_xsd.open010 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    open_com_element=AnyElement(
        children=[
            AnyElement(
                qname='{http://open.com/}extra',
                text='1'
            ),
            AnyElement(
                qname='{http://open.com/}extra',
                text='1'
            ),
        ]
    )
)
