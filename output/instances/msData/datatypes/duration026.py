from output.models.ms_data.datatypes.duration_xsd.duration import ComplexTest
from output.models.ms_data.datatypes.duration_xsd.duration import Root
from output.models.ms_data.datatypes.duration_xsd.duration import SimpleTest
from xsdata.models.datatype import XmlDuration


obj = Root(
    complex_test=ComplexTest(
        comp_foo=XmlDuration("P2000Y2M29DT10H30M")
    ),
    simple_test=SimpleTest(
        value=XmlDuration("P2000Y2M29DT10H30M")
    )
)
