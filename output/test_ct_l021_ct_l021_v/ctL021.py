from output.models.ms_data.complex_type.ct_l021_xsd.ct_l021 import FooTest
from output.models.ms_data.complex_type.ct_l021_xsd.ct_l021 import Root


obj = Root(
    foo_test=FooTest(
        child_1='info',
        child_2=3,
        other_attributes={
            '{myNamespace}testAttr': 'Test Attribute',
        }
    )
)
