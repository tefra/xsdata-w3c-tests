from output.models.ms_data.wildcards.wild_g023_xsd.wild_g023 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    foobar_element=AnyElement(
        qname="{http://foobar}bar",
        text="foo bar"
    )
)
