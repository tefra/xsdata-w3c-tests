from output.models.ms_data.datatypes.hex_binary_xsd.hex_binary import ComplexTest
from output.models.ms_data.datatypes.hex_binary_xsd.hex_binary import Root
from output.models.ms_data.datatypes.hex_binary_xsd.hex_binary import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=b''
    ),
    simple_test=SimpleTest(

    )
)
