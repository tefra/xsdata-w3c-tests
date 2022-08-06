from output.models.ms_data.regex.re_k88_xsd.re_k88 import Doc
from output.models.ms_data.regex.re_k88_xsd.re_k88 import Regex


obj = Doc(
    elem=[
        Regex(
            att="a"
        ),
        Regex(
            att="&amp;"
        ),
        Regex(
            att="́"
        ),
        Regex(
            att="𐀀"
        ),
    ]
)
