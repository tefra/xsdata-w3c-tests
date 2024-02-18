from output.models.ms_data.datatypes.any_uri_xsd.any_uri import ComplexTest
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import Root
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo='telnet://melvyl.ucop.edu/'
    ),
    simple_test=SimpleTest(
        value='telnet://melvyl.ucop.edu/'
    )
)
