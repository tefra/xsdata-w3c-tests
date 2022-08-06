from output.models.ms_data.wildcards.wild_z004_xsd.wild_z004 import CtypeFoo
from output.models.ms_data.wildcards.wild_z004_xsd.wild_z004 import RootElem
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = RootElem(
    any_element=DerivedElement(
        qname="{http://xsdtesting}myelem",
        value=CtypeFoo(
            a="hello"
        ),
        type="{http://xsdtesting}ctype_foo"
    )
)
