from output.models.ms_data.simple_type.st_g012_xsd.st_g012 import FooTest
from output.models.ms_data.simple_type.st_g012_xsd.st_g012 import Root


obj = Root(
    foo_test=FooTest(
        value=[
            'CA',
        ]
    )
)
