from output.models.ms_data.datatypes.string_xsd.string import ComplexTest
from output.models.ms_data.datatypes.string_xsd.string import Root
from output.models.ms_data.datatypes.string_xsd.string import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo='!$%%*))*('
    ),
    simple_test=SimpleTest(
        value='!$%%*))*('
    )
)
