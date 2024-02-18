from output.models.ms_data.simple_type.st_g010_xsd.st_g010 import FooTest
from output.models.ms_data.simple_type.st_g010_xsd.st_g010 import FooType
from output.models.ms_data.simple_type.st_g010_xsd.st_g010 import Root


obj = Root(
    foo_test=FooTest(
        value=FooType.CA
    )
)
