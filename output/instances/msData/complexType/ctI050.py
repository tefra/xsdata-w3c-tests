from output.models.ms_data.complex_type.ct_i050_xsd.ct_i050 import FooTest
from output.models.ms_data.complex_type.ct_i050_xsd.ct_i050 import Root


obj = Root(
    foo_test=FooTest(
        foo_ele1='string',
        foo_ele2=26,
        foo_ele3=True
    )
)
