from output.models.ms_data.regex.p17_xsd.p17 import Doc
from output.models.ms_data.regex.p17_xsd.p17 import Regex


obj = Doc(
    elem=[
        Regex(
            att='abcaabbccabc'
        ),
    ]
)
