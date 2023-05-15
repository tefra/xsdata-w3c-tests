from output.models.ms_data.wildcards.wild_g033_xsd.wild_g033 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    local_foobar_element=AnyElement(
        qname="{http://foobar}bar",
        text="foo bar"
    )
)
