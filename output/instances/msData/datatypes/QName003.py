from output.models.ms_data.datatypes.qname_xsd.qname import ComplexTest
from output.models.ms_data.datatypes.qname_xsd.qname import Root
from xml.etree.ElementTree import QName


obj = Root(
    complex_test=ComplexTest(
        comp_foo=QName("fo124")
    ),
    simple_test=QName("fo124")
)