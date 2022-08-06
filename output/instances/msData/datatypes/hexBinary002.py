from output.models.ms_data.datatypes.hex_binary002_xsd.hex_binary002 import ComplexTest
from output.models.ms_data.datatypes.hex_binary002_xsd.hex_binary002 import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            b"\x124Vx\xab\xcd\xef",
        ]
    ),
    simple_test=[
        b"\x124Vx\xab\xcd\xef",
    ]
)
