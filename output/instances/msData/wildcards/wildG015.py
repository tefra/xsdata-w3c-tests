from output.models.ms_data.wildcards.wild_g015_xsd.wild_g015 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    any_element=AnyElement(
        qname="{http://foobar}bar",
        text="bar",
        tail=None,
        children=[],
        attributes={}
    )
)
