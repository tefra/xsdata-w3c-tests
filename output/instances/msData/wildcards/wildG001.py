from output.models.ms_data.wildcards.wild_g001_xsd.wild_g001 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    any_element=AnyElement(
        qname="{http://foobar}bar",
        text="foo bar",
        tail=None,
        children=[],
        attributes={}
    )
)
