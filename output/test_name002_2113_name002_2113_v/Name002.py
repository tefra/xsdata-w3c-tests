from output.models.ms_data.datatypes.name_xsd.name import ComplexTest
from output.models.ms_data.datatypes.name_xsd.name import Root
from output.models.ms_data.datatypes.name_xsd.name import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo='_foo'
    ),
    simple_test=SimpleTest(
        value='_foo'
    )
)
