from output.models.ms_data.attribute.att_d004_xsd.att_d004 import AttRef
from output.models.ms_data.attribute.att_d004_xsd.att_d004 import Doc
from output.models.ms_data.attribute.att_d004_xsd.att_d004 import List


obj = Doc(
    elem=AttRef(
        att1=[
            List.VALUE_1,
            List.VALUE_2,
            List.VALUE_5,
        ]
    )
)
