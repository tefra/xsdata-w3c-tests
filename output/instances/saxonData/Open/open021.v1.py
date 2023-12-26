from output.models.saxon_data.open.open021_xsd.open021 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        '\n  o-O-o\n  ',
        AnyElement(
            qname='{http://open.com/}extra',
            text='42',
            tail='\n  o-O-o  \n  '
        ),
        AnyElement(
            qname='{http://open.com/}extra',
            text='97',
            tail=' \n  o-O-o   \n'
        ),
    ]
)
