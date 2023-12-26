from output.models.sun_data.combined.xsd002.xsd002_xsd.xsd002 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    foo_or_bar_or_zot=[
        AnyElement(
            qname='foo',
            text='',
            children=[
                AnyElement(
                    qname='this',
                    text=''
                ),
                AnyElement(
                    qname='contents',
                    text='',
                    tail='\n\t\tshould not be\n\t\tvalidated\n\t\t'
                ),
                AnyElement(
                    qname='because',
                    text='',
                    attributes={
                        'it': 'is ur-type',
                    }
                ),
            ]
        ),
        AnyElement(
            qname='{http://foo.com}bar',
            text=''
        ),
        AnyElement(
            qname='zot',
            text='\n\t\twhen using ',
            children=[
                AnyElement(
                    qname='ur',
                    text='',
                    children=[
                        AnyElement(
                            qname='type',
                            text=''
                        ),
                    ]
                ),
            ],
            attributes={
                'attributes': 'are',
                'also': 'ignored',
            }
        ),
    ]
)
