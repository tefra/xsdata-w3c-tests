from output.models.wg_data.sg.snneg_xsd.snneg import Test
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Test(
    s1=None,
    s="Test case for interaction of substitution groups and &#10;   #definedSibling.",
    n="",
    any_element=[
        AnyElement(
            qname="{http://www.w3.org/XML/2008/xsdl-exx/ns1}e",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
