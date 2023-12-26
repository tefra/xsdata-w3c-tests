from output.models.ms_data.regex.p13_xsd.p13 import Doc
from output.models.ms_data.regex.p13_xsd.p13 import Regex


obj = Doc(
    elem=[
        Regex(
            att='abcaabbccabc'
        ),
    ]
)
