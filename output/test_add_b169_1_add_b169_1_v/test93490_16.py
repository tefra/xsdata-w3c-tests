from output.models.ms_data.additional.test93490_16_xsd.test93490_16 import MapInfo
from output.models.ms_data.additional.test93490_16_xsd.test93490_16 import SchemaType
from xsdata.formats.dataclass.models.generics import AnyElement


obj = MapInfo(
    schema=[
        SchemaType(
            any_element=[
                AnyElement(
                    qname='{http://www.w3.org/2001/XMLSchema}schema',
                    text='',
                    children=[
                        AnyElement(
                            qname='{http://www.w3.org/2001/XMLSchema}import',
                            text='',
                            attributes={
                                'namespace': 'http://schemas.microsoft.com/office/excel/2003/xml',
                                'schemaLocation': 'test93490_16.xsd',
                            }
                        ),
                        AnyElement(
                            qname='{http://www.w3.org/2001/XMLSchema}element',
                            text='',
                            children=[
                                AnyElement(
                                    qname='{http://www.w3.org/2001/XMLSchema}complexType',
                                    text='',
                                    children=[
                                        AnyElement(
                                            qname='{http://www.w3.org/2001/XMLSchema}all',
                                            text='',
                                            children=[
                                                AnyElement(
                                                    qname='{http://www.w3.org/2001/XMLSchema}element',
                                                    text='',
                                                    attributes={
                                                        'name': 'NS2item1',
                                                        'type': '{http://www.w3.org/2001/XMLSchema}string',
                                                    }
                                                ),
                                                AnyElement(
                                                    qname='{http://www.w3.org/2001/XMLSchema}element',
                                                    text='',
                                                    attributes={
                                                        'name': 'NS2item2',
                                                        'type': '{http://www.w3.org/2001/XMLSchema}string',
                                                    }
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ],
                            attributes={
                                'name': 'SAPCodeType',
                            }
                        ),
                    ],
                    attributes={
                        'targetNamespace': 'http://www.mydefaultnamespace.com/SAP',
                        'elementFormDefault': 'qualified',
                    }
                ),
                AnyElement(
                    qname='a',
                    text=''
                ),
            ],
            id='Schema3',
            namespace='http://www.mydefaultnamespace.com/SAP'
        ),
    ],
    selection_namespaces='http://foo'
)
