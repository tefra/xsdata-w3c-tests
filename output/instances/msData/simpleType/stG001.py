from output.models.ms_data.simple_type.st_g001_xsd.st_g001 import FooTest
from output.models.ms_data.simple_type.st_g001_xsd.st_g001 import Root


obj = Root(
    foo_test=FooTest(
        value=[
            25,
            33,
            123456789012345678,
        ]
    )
)
