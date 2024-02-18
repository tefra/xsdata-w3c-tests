from output.models.ms_data.datatypes.duration_xsd.duration import ComplexTest
from output.models.ms_data.datatypes.duration_xsd.duration import Root
from output.models.ms_data.datatypes.duration_xsd.duration import SimpleTest
from xsdata.models.datatype import XmlDuration


obj = Root(
    complex_test=ComplexTest(
        comp_foo=XmlDuration("P0Y0M3D")
    ),
    simple_test=SimpleTest(
        value=XmlDuration("P0Y0M3D")
    )
)
