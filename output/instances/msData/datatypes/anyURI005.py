from output.models.ms_data.datatypes.any_uri_xsd.any_uri import ComplexTest
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo='ftp://ftp.is.co.za/rfc/rfc1808.txt'
    ),
    simple_test='ftp://ftp.is.co.za/rfc/rfc1808.txt'
)
