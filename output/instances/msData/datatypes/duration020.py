from output.models.ms_data.datatypes.duration_xsd.duration import ComplexTest
from output.models.ms_data.datatypes.duration_xsd.duration import Root
from xsdata.models.datatype import XmlDuration


obj = Root(
    complex_test=ComplexTest(
        comp_foo=XmlDuration("P0Y0M0DT0H0M0.0001S")
    ),
    simple_test=XmlDuration("P0Y0M0DT0H0M0.0001S")
)
