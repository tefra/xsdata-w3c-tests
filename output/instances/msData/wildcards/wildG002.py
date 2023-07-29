from output.models.ms_data.wildcards.wild_g002_xsd.wild_g002 import Foo
from output.models.ms_data.wildcards.wild_g002_xsd.wild_g002a import Bar


obj = Foo(
    any_element=Bar(
        value="foo bar"
    )
)
