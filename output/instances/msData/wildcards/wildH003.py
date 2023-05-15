from output.models.ms_data.wildcards.wild_h003_xsd.wild_h003 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    target_namespace_element=AnyElement(
        qname="{http://foobar}bar",
        text="foo bar"
    )
)
