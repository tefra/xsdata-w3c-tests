from output.models.ms_data.simple_type.st_h003_xsd.st_h003 import FooTest
from output.models.ms_data.simple_type.st_h003_xsd.st_h003 import Root


obj = Root(
    foo_test=FooTest(
        value=[
            '12345',
        ]
    )
)
