from output.models.ms_data.complex_type.ct_l016_xsd.ct_l016 import FooTest
from output.models.ms_data.complex_type.ct_l016_xsd.ct_l016 import Root


obj = Root(
    foo_test=FooTest(
        child_1='info',
        child_2=3,
        other_attributes={
            '{http://www.dummy.com}testAttr': 'Test Attribute',
        }
    )
)
