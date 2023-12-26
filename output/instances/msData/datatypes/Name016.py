from output.models.ms_data.datatypes.name_xsd.name import ComplexTest
from output.models.ms_data.datatypes.name_xsd.name import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo='fo:fo_124-.s:da3'
    ),
    simple_test='fo:fo_124-.s:da3'
)
