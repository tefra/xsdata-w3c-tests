from output.models.ms_data.datatypes.any_uri_xsd.any_uri import ComplexTest
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo='gopher://spinaltap.micro.umn.edu/00/Weather/California/Los%20Angeles'
    ),
    simple_test='gopher://spinaltap.micro.umn.edu/00/Weather/California/Los%20Angeles'
)
