from output.models.ms_data.wildcards.wild_g035_xsd.wild_g035 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    local_w3_org_1999_xhtml_element=AnyElement(
        qname="bar",
        text="foo bar",
        tail=None,
        children=[],
        attributes={}
    )
)
