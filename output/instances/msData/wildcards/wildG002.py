from output.models.ms_data.wildcards.wild_g002_xsd.wild_g002 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    any_element=AnyElement(
        qname="{http://foo}bar",
        text="foo bar"
    )
)
