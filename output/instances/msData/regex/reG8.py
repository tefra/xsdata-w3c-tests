from output.models.ms_data.regex.re_g8_xsd.re_g8 import Doc
from output.models.ms_data.regex.re_g8_xsd.re_g8 import Regex


obj = Doc(
    elem=[
        Regex(
            att="1234567890:;&lt;=&gt;?@Azaz"
        ),
    ]
)
