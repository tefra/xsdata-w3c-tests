from output.models.ms_data.complex_type.ct_l017_xsd.ct_l017 import FooTest
from output.models.ms_data.complex_type.ct_l017_xsd.ct_l017 import Root


obj = Root(
    foo_test=FooTest(
        child_1="info",
        child_2=3
    )
)
