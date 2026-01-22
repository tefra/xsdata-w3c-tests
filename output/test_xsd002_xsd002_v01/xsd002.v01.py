from output.models.sun_data.combined.xsd002.xsd002_xsd.xsd002 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    foo_or_bar_or_zot=[
        Root.Foo(
            content=AnyElement(
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
            )
        ),
        Root.Bar(

        ),
        Root.Zot(
            content=AnyElement(
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
            )
        ),
    ]
)
