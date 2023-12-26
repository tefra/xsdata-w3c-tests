from output.models.ms_data.wildcards.wild_i012_xsd.wild_i012 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    other_element=AnyElement(
        children=[
            AnyElement(
                qname='{A}b',
                text='test'
            ),
            AnyElement(
                qname='{A}b',
                text='test'
            ),
            AnyElement(
                qname='{A}b',
                text='test'
            ),
        ]
    )
)
