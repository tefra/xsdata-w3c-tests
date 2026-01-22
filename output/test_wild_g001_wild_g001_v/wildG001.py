from output.models.ms_data.wildcards.wild_g001_xsd.wild_g001 import Bar
from output.models.ms_data.wildcards.wild_g001_xsd.wild_g001 import Foo


obj = Foo(
    any_element=Bar(
        value='foo bar'
    )
)
