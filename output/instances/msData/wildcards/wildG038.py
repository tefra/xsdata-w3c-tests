from output.models.ms_data.wildcards.wild_g038_xsd.wild_g038 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    target_namespace_w3_org_1999_xhtml_element=AnyElement(
        qname="{http://foobar}bar",
        text="foo bar",
        tail=None,
        children=[],
        attributes={}
    )
)
