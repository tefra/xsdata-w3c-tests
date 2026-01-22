from output.models.saxon_data.all.all306_xsd.all306 import B
from output.models.saxon_data.all.all306_xsd.all306 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        B(
            content=[
                None,
            ]
        ),
        'text',
        AnyElement(
            qname='a',
            text='',
            tail='text'
        ),
        AnyElement(
            qname='d',
            text='',
            tail='text'
        ),
        AnyElement(
            qname='a',
            text=''
        ),
    ]
)
