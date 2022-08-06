from output.models.ms_data.datatypes.base64_binary002_xsd.base64_binary002 import ComplexTest
from output.models.ms_data.datatypes.base64_binary002_xsd.base64_binary002 import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            b"\x01\x02\x03",
        ]
    ),
    simple_test=[
        b"\x01\x02\x03",
    ]
)
