from output.models.ms_data.datatypes.unsigned_long007_xsd.unsigned_long007 import ComplexTest
from output.models.ms_data.datatypes.unsigned_long007_xsd.unsigned_long007 import Root
from output.models.ms_data.datatypes.unsigned_long007_xsd.unsigned_long007 import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            1844674407370955161,
        ]
    ),
    simple_test=SimpleTest(
        value=[
            1844674407370955161,
        ]
    )
)
