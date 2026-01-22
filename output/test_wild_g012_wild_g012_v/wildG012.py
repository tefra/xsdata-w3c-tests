from output.models.ms_data.wildcards.wild_g012_xsd.wild_g012 import Bar
from output.models.ms_data.wildcards.wild_g012_xsd.wild_g012 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    target_namespace_w3_org_1999_xhtml_element=Bar(
        any_element=AnyElement(
            text='foo bar'
        )
    )
)
