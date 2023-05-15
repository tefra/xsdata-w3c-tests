from output.models.ms_data.wildcards.wild_g027_xsd.wild_g027 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    target_namespace_element=AnyElement(
        qname="{http://foobar}bar",
        text="foo bar"
    )
)
