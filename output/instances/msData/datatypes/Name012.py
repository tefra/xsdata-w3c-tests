from output.models.ms_data.datatypes.name_xsd.name import ComplexTest
from output.models.ms_data.datatypes.name_xsd.name import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo='fo:1fo'
    ),
    simple_test='fo:1fo'
)
