from output.models.wg_data.sg.negsn_xsd.negsn import E
from output.models.wg_data.sg.negsn_xsd.negsn import Test
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Test(
    any_element=E(
        value="Test case for interaction of substitution groups and &#10;   #definedSibling."
    ),
    s1_or_s=DerivedElement(
        qname="{http://www.w3.org/XML/2008/xsdl-exx/ns1}s",
        value=""
    ),
    n=""
)
