from output.models.ms_data.regex.re_i82_xsd.re_i82 import Doc
from output.models.ms_data.regex.re_i82_xsd.re_i82 import Regex


obj = Doc(
    elem=[
        Regex(
            att="\.,\s,\S,\i,\I,\c,\C,\d,\D,\w,\W"
        ),
    ]
)
