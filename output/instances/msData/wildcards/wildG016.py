from output.models.ms_data.wildcards.wild_g016_xsd.wild_g016 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    any_element=AnyElement(
        qname="{http://bar}bar",
        text="foo bar"
    )
)
