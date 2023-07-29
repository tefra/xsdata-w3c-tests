from output.models.ms_data.wildcards.wild_g013_xsd.wild_g013 import B
from output.models.ms_data.wildcards.wild_g013_xsd.wild_g013 import Foo
from output.models.ms_data.wildcards.wild_g013_xsd.wild_g013_imp import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    target_namespace_w3_org_1999_xhtml_element=[
        Foo(
            any_element=AnyElement(
                text="foo bar"
            )
        ),
        B(
            value="testing"
        ),
        Foo(
            any_element=AnyElement(
                text="foo bar"
            )
        ),
        Foo(
            any_element=AnyElement(
                text="foo bar"
            )
        ),
        B(
            value="testing"
        ),
        B(
            value="testing"
        ),
    ]
)
