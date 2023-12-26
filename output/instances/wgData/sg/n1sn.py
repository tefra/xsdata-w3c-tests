from output.models.wg_data.sg.negsn_xsd.negsn import N1
from output.models.wg_data.sg.negsn_xsd.negsn import Test
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Test(
    any_element=N1(
        value='Test case for interaction of substitution groups and \n   #definedSibling.'
    ),
    s1_or_s=DerivedElement(
        qname='{http://www.w3.org/XML/2008/xsdl-exx/ns1}s',
        value=''
    ),
    n=''
)
