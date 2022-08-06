from output.models.ms_data.wildcards.wild_g006_xsd.wild_g006 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    local_element=AnyElement(
        qname="bar",
        text="foo bar",
        tail=None,
        children=[],
        attributes={}
    )
)
