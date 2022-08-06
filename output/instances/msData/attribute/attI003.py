from output.models.ms_data.attribute.att_i003_xsd.att_i003 import AttRef
from output.models.ms_data.attribute.att_i003_xsd.att_i003 import AttRefAtt1
from output.models.ms_data.attribute.att_i003_xsd.att_i003 import Doc


obj = Doc(
    elem=AttRef(
        att1=AttRefAtt1.AK,
        att2=123
    )
)
