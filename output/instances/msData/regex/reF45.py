from output.models.ms_data.regex.re_f45_xsd.re_f45 import Doc
from output.models.ms_data.regex.re_f45_xsd.re_f45 import Regex


obj = Doc(
    elem=[
        Regex(
            att="a+*abc"
        ),
    ]
)
