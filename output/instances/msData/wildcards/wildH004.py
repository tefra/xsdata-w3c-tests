from output.models.ms_data.wildcards.wild_h004_xsd.wild_h004 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    target_namespace_element=AnyElement(
        qname="{http://foobar}bar",
        text="foo bar",
        tail=None,
        children=[],
        attributes={}
    )
)
