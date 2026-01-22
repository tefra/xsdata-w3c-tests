from output.models.ms_data.model_groups.mg_i010_xsd.mg_i010 import Doc
from output.models.ms_data.model_groups.mg_i010_xsd.mg_i010 import Foo


obj = Doc(
    choice=[
        Foo.B(
            value='I am a stringy string'
        ),
    ]
)
