from output.models.ms_data.datatypes.duration027_xsd.duration027 import ComplexTest
from output.models.ms_data.datatypes.duration027_xsd.duration027 import Root
from xsdata.models.datatype import XmlDuration


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            XmlDuration("P2000Y2M29DT10H30M"),
        ]
    ),
    simple_test=[
        XmlDuration("P2000Y2M29DT10H30M"),
    ]
)
