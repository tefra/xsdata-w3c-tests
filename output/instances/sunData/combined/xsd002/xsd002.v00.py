from output.models.sun_data.combined.xsd002.xsd002_xsd.xsd002 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    foo_or_bar_or_zot=[
        AnyElement(
            qname='foo',
            text=''
        ),
        AnyElement(
            qname='{http://foo.com}bar',
            text=''
        ),
        AnyElement(
            qname='zot',
            text=''
        ),
        AnyElement(
            qname='foo',
            text=''
        ),
        AnyElement(
            qname='{http://foo.com}bar',
            text=''
        ),
        AnyElement(
            qname='zot',
            text=''
        ),
    ]
)
