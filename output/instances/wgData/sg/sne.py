from output.models.wg_data.sg.snneg_xsd.snneg import E
from output.models.wg_data.sg.snneg_xsd.snneg import Test
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Test(
    s1_or_s=DerivedElement(
        qname="{http://www.w3.org/XML/2008/xsdl-exx/ns1}s",
        value="Test case for interaction of substitution groups and &#10;   #definedSibling."
    ),
    n="",
    any_element=[
        E(

        ),
    ]
)
