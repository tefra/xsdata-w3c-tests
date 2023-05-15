from output.models.ms_data.wildcards.wild_h010_xsd.wild_h010 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    w3_org_1999_xhtml_element=AnyElement(
        qname="{http://www.w3.org/1999/xhtml}bar",
        text="foo bar"
    )
)
