from output.models.ms_data.simple_type.st_g006_xsd.st_g006 import FooTest
from output.models.ms_data.simple_type.st_g006_xsd.st_g006 import Root


obj = Root(
    foo_test=FooTest(
        value=[
            10,
            123456789012345678,
        ]
    )
)
