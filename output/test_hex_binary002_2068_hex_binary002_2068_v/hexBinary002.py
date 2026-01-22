from output.models.ms_data.datatypes.hex_binary002_xsd.hex_binary002 import ComplexTest
from output.models.ms_data.datatypes.hex_binary002_xsd.hex_binary002 import Root
from output.models.ms_data.datatypes.hex_binary002_xsd.hex_binary002 import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            b'\x124Vx\xab\xcd\xef',
        ]
    ),
    simple_test=SimpleTest(
        value=[
            b'\x124Vx\xab\xcd\xef',
        ]
    )
)
