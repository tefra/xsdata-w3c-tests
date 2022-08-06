from output.models.ms_data.attribute.att_d004_xsd.att_d004 import AttRef
from output.models.ms_data.attribute.att_d004_xsd.att_d004 import Doc
from output.models.ms_data.attribute.att_d004_xsd.att_d004 import ListType


obj = Doc(
    elem=AttRef(
        att1=[
            ListType.VALUE_1,
            ListType.VALUE_2,
            ListType.VALUE_5,
        ]
    )
)
