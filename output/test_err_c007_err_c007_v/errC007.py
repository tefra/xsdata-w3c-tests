from output.models.ms_data.errata10.err_c007_xsd.err_c007 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    local_element1=AnyElement(
        qname='localElement1',
        text='',
        children=[
            AnyElement(
                qname='{http://www.tempuri.org}testContent',
                text='123'
            ),
        ],
        attributes={
            'attr': 'testValue',
        }
    ),
    local_element2=AnyElement(
        qname='localElement2',
        text='',
        children=[
            AnyElement(
                qname='testContent',
                text='any text'
            ),
            AnyElement(
                qname='{http://www.tempuri.org}testContent',
                text='456'
            ),
        ],
        attributes={
            '{http://www.tempuri.org}testAttribute': 'true',
        }
    )
)
