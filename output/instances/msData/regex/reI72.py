from output.models.ms_data.regex.re_i72_xsd.re_i72 import Doc
from output.models.ms_data.regex.re_i72_xsd.re_i72 import Regex


obj = Doc(
    elem=[
        Regex(
            att="&#9;a &#10;&#13;&#10; &#13;&#9;b"
        ),
    ]
)
