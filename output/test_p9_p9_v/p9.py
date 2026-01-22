from output.models.ms_data.regex.p9_xsd.p9 import Doc
from output.models.ms_data.regex.p9_xsd.p9 import MyEnum
from output.models.ms_data.regex.p9_xsd.p9 import Regex


obj = Doc(
    elem=[
        Regex(
            att=MyEnum.VALUE_1
        ),
    ]
)
