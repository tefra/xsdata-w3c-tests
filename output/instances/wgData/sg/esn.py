from output.models.wg_data.sg.negsn_xsd.negsn import Test
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Test(
    any_element=AnyElement(
        qname="{http://www.w3.org/XML/2008/xsdl-exx/ns1}e",
        text="Test case for interaction of substitution groups and &#10;   #definedSibling.",
        tail=None,
        children=[],
        attributes={}
    ),
    s1=None,
    s="",
    n=""
)
