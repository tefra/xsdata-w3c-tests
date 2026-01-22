from output.models.ms_data.complex_type.ct_l003_xsd.ct_l003 import FooTest
from output.models.ms_data.complex_type.ct_l003_xsd.ct_l003 import Root


obj = Root(
    foo_test=FooTest(
        value='\n\t',
        my_attr='test Attribute'
    )
)
