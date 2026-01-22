from output.models.sun_data.combined.identity.idc006.idc006_nogen_xsd.idc006_nogen import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    keys=Root.Keys(
        any_element=[
            AnyElement(
                qname='{http://www.publishing.org}a',
                text='',
                children=[
                    AnyElement(
                        qname='{http://www.publishing.org}a',
                        text='',
                        children=[
                            AnyElement(
                                qname='{http://www.publishing.org}b',
                                text='',
                                children=[
                                    AnyElement(
                                        qname='{http://www.publishing.org}b',
                                        text='',
                                        attributes={
                                            'id': 'id2',
                                        }
                                    ),
                                ],
                                attributes={
                                    'id': 'id1',
                                }
                            ),
                        ]
                    ),
                ]
            ),
        ]
    ),
    keyref=[
        'id1',
        'id2',
    ]
)
