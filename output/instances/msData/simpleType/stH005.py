from output.models.ms_data.simple_type.st_h005_xsd.st_h005 import FooTest
from output.models.ms_data.simple_type.st_h005_xsd.st_h005 import Root


obj = Root(
    foo_test=FooTest(
        value=[
            '12345',
        ]
    )
)
