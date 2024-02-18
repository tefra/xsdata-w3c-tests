from output.models.ms_data.datatypes.unsigned_int007_xsd.unsigned_int007 import ComplexTest
from output.models.ms_data.datatypes.unsigned_int007_xsd.unsigned_int007 import Root
from output.models.ms_data.datatypes.unsigned_int007_xsd.unsigned_int007 import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            429496729,
        ]
    ),
    simple_test=SimpleTest(
        value=[
            429496729,
        ]
    )
)
