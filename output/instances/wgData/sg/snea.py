from output.models.wg_data.sg.snbranch_xsd.snbranch import Test
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Test(
    choice=[
        DerivedElement(
            qname="{http://www.w3.org/XML/2008/xsdl-exx/ns1}s",
            value="Test case for interaction of substitution groups and &#10;   #definedSibling.",
            type=None
        ),
        DerivedElement(
            qname="{http://www.w3.org/XML/2008/xsdl-exx/ns1}n",
            value="",
            type=None
        ),
        AnyElement(
            qname="{http://www.w3.org/XML/2008/xsdl-exx/ns1}e",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        DerivedElement(
            qname="{http://www.w3.org/XML/2008/xsdl-exx/ns1}a",
            value="",
            type=None
        ),
    ]
)