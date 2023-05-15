from output.models.ms_data.wildcards.wild_h011_xsd.wild_h011 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    w3_org_1999_xhtml_element=AnyElement(
        qname="{http://www.w3.org/1999/xhtml}b",
        text="foo bar"
    )
)
