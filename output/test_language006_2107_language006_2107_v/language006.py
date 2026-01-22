from output.models.ms_data.datatypes.language_xsd.language import ComplexTest
from output.models.ms_data.datatypes.language_xsd.language import Root
from output.models.ms_data.datatypes.language_xsd.language import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo='spanish'
    ),
    simple_test=SimpleTest(
        value='spanish'
    )
)
