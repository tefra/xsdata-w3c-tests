from output.models.ms_data.complex_type.ct_l008_xsd.ct_l008 import FooTest
from output.models.ms_data.complex_type.ct_l008_xsd.ct_l008 import Root


obj = Root(
    foo_test=FooTest(
        child_1="info",
        child_2=3
    )
)
