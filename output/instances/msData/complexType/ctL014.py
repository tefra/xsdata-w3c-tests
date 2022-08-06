from output.models.ms_data.complex_type.ct_l014_xsd.ct_l014 import FooTest
from output.models.ms_data.complex_type.ct_l014_xsd.ct_l014 import Root


obj = Root(
    foo_test=FooTest(
        child_1="info",
        child_2=3,
        my_attr=12
    )
)
