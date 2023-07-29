from output.models.ms_data.model_groups.mg_m013_xsd.mg_m013 import Doc
from output.models.ms_data.model_groups.mg_m013_xsd.mg_m013 import Foo
from output.models.ms_data.model_groups.mg_m013_xsd.mg_m013 import Global
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    any_element=AnyElement(
        children=[
            Foo(
                e1="",
                e2=""
            ),
            Global(

            ),
        ]
    )
)
