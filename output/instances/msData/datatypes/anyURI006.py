from output.models.ms_data.datatypes.any_uri_xsd.any_uri import ComplexTest
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import Root
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo='gopher://spinaltap.micro.umn.edu/00/Weather/California/Los%20Angeles'
    ),
    simple_test=SimpleTest(
        value='gopher://spinaltap.micro.umn.edu/00/Weather/California/Los%20Angeles'
    )
)
