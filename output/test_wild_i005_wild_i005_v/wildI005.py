from output.models.ms_data.wildcards.wild_i005_xsd.wild_i005 import Bar
from output.models.ms_data.wildcards.wild_i005_xsd.wild_i005 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    foo_element=[
        AnyElement(
            qname='{foo}b',
            text='test'
        ),
        AnyElement(
            qname='{foo}b',
            text='test'
        ),
    ],
    a_element=[
        AnyElement(
            qname='{a}b',
            text='test'
        ),
        AnyElement(
            qname='{a}b',
            text='test'
        ),
    ],
    b_element=[
        AnyElement(
            qname='{b}b',
            text='test'
        ),
        AnyElement(
            qname='{b}b',
            text='test'
        ),
    ],
    target_namespace_element=AnyElement(
        children=[
            Bar(

            ),
            Bar(

            ),
            AnyElement(
                qname='{http://foo}foo',
                text=' test'
            ),
        ]
    )
)
