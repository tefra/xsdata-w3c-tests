from output.models.ms_data.regex.re_i83_xsd.re_i83 import Doc
from output.models.ms_data.regex.re_i83_xsd.re_i83 import Regex


obj = Doc(
    elem=[
        Regex(
            att='\\.abcd,\\sssss,\\SSSSSS,\\iiiiiii,\\,\\c,\\CCCCCC,\\ddd,\\D,\\wwwwwww,\\WWW'
        ),
    ]
)
