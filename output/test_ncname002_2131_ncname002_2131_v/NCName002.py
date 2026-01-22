from output.models.ms_data.datatypes.ncname_xsd.ncname import ComplexTest
from output.models.ms_data.datatypes.ncname_xsd.ncname import Root
from output.models.ms_data.datatypes.ncname_xsd.ncname import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo='_foo'
    ),
    simple_test=SimpleTest(
        value='_foo'
    )
)
