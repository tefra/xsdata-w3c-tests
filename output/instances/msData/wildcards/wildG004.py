from output.models.ms_data.wildcards.wild_g004_xsd.wild_g004 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    other_element=AnyElement(
        qname="{http://foo}bar",
        text="foo bar",
        tail=None,
        children=[],
        attributes={}
    )
)
