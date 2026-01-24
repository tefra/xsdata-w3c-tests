from output.models.ms_data.model_groups.mg_q003_xsd.mg_q003 import Doc
from output.models.ms_data.model_groups.mg_q003_xsd.mg_q003 import Foo


obj = Doc(
    e1_or_e2=[
        Foo.E1(
            value='yo'
        ),
        Foo.E2(
            value='eh?'
        ),
        Foo.E1(
            value='YO!'
        ),
    ]
)
