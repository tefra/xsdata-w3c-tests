from output.models.ms_data.simple_type.st_h007_xsd.st_h007 import FooTest
from output.models.ms_data.simple_type.st_h007_xsd.st_h007 import FooType
from output.models.ms_data.simple_type.st_h007_xsd.st_h007 import Root


obj = Root(
    foo_test=FooTest(
        value=FooType.CA
    )
)
