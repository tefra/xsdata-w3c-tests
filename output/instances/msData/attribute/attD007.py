from output.models.ms_data.attribute.att_d007_xsd.att_d007 import AttRef
from output.models.ms_data.attribute.att_d007_xsd.att_d007 import Char
from output.models.ms_data.attribute.att_d007_xsd.att_d007 import Doc


obj = Doc(
    elem=AttRef(
        att1=[
            Char.A,
            Char.B,
            Char.C,
            Char.D,
            Char.E,
        ]
    )
)
