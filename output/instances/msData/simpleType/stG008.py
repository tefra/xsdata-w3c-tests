from output.models.ms_data.simple_type.st_g008_xsd.st_g008 import FooTest
from output.models.ms_data.simple_type.st_g008_xsd.st_g008 import Root


obj = Root(
    foo_test=FooTest(
        value=[
            10,
            20,
            55,
        ]
    )
)
