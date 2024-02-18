from output.models.ms_data.datatypes.long_xsd.long import ComplexTest
from output.models.ms_data.datatypes.long_xsd.long import Root
from output.models.ms_data.datatypes.long_xsd.long import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=-1
    ),
    simple_test=SimpleTest(
        value=-1
    )
)
