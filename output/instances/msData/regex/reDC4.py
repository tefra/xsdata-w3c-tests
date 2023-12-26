from output.models.ms_data.regex.re_dc4_xsd.re_dc4 import Doc
from output.models.ms_data.regex.re_dc4_xsd.re_dc4 import Regex


obj = Doc(
    elem=[
        Regex(
            att='http://www.foo.com'
        ),
    ]
)
