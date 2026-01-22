from output.models.saxon_data.all.all005_xsd.all005 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        AnyElement(
            qname='{http://a.ns/}wasp',
            text=''
        ),
        AnyElement(
            qname='{http://b.ns/}bee',
            text=''
        ),
        AnyElement(
            qname='{http://a.ns/}ant',
            text=''
        ),
        AnyElement(
            qname='{http://b.ns/}beetle',
            text=''
        ),
        AnyElement(
            qname='{http://a.ns/}earwig',
            text=''
        ),
        AnyElement(
            qname='{http://b.ns/}maybug',
            text=''
        ),
    ]
)
