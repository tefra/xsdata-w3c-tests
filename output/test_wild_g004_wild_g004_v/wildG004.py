from output.models.ms_data.wildcards.wild_g004_xsd.wild_g004 import Foo
from output.models.ms_data.wildcards.wild_g004_xsd.wild_g004a import Bar


obj = Foo(
    other_element=Bar(
        value='foo bar'
    )
)
