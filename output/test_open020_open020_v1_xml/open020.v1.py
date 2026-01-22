from output.models.saxon_data.open.open020_xsd.open020 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
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
