from output.models.ms_data.datatypes.g_day_xsd.g_day import ComplexTest
from output.models.ms_data.datatypes.g_day_xsd.g_day import Root
from output.models.ms_data.datatypes.g_day_xsd.g_day import SimpleTest
from xsdata.models.datatype import XmlPeriod


obj = Root(
    complex_test=ComplexTest(
        comp_foo=XmlPeriod("---15")
    ),
    simple_test=SimpleTest(
        value=XmlPeriod("---15")
    )
)
