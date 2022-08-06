from output.models.ms_data.wildcards.wild_g040_xsd.wild_g040 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    target_namespace_element=AnyElement(
        qname="{http://www.w3.org/1999/xhtml}b",
        text="foo bar",
        tail=None,
        children=[],
        attributes={}
    )
)
