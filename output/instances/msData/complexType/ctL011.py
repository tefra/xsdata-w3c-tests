from output.models.ms_data.complex_type.ct_l011_xsd.ct_l011 import FooTest
from output.models.ms_data.complex_type.ct_l011_xsd.ct_l011 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    foo_test=FooTest(
        content=[
            '\n\tmixed content\n\t',
            AnyElement(
                qname='child_1',
                text='info'
            ),
            '\n        for fooTest\n\t',
            AnyElement(
                qname='child_2',
                text='3'
            ),
        ]
    )
)
