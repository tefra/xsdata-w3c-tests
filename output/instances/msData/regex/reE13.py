from output.models.ms_data.regex.re_e13_xsd.re_e13 import Doc
from output.models.ms_data.regex.re_e13_xsd.re_e13 import Regex


obj = Doc(
    elem=[
        Regex(
            att='.\\?*+{}[]()|'
        ),
    ]
)
