from output.models.ms_data.regex.re_g14_xsd.re_g14 import Doc
from output.models.ms_data.regex.re_g14_xsd.re_g14 import Regex


obj = Doc(
    elem=[
        Regex(
            att='\\|.?*+(){}-[]^'
        ),
    ]
)
