from output.models.ms_data.simple_type.st_z031_xsd.st_z031 import ComplexTest
from output.models.ms_data.simple_type.st_z031_xsd.st_z031 import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo='fo:foo'
    ),
    simple_test='fo:foo'
)
