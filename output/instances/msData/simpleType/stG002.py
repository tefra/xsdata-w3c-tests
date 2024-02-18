from output.models.ms_data.simple_type.st_g002_xsd.st_g002 import FooTest
from output.models.ms_data.simple_type.st_g002_xsd.st_g002 import Root


obj = Root(
    foo_test=FooTest(
        value=[
            10,
            25,
            33,
        ]
    )
)
