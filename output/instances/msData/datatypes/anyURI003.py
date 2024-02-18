from output.models.ms_data.datatypes.any_uri_xsd.any_uri import ComplexTest
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import Root
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo='http://www.w3.org/1999/XMLSchema'
    ),
    simple_test=SimpleTest(
        value='http://www.w3.org/1999/XMLSchema'
    )
)
