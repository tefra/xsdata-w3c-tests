from output.models.ms_data.attribute_group.attg_d033_xsd.attg_d033 import AttRef
from output.models.ms_data.attribute_group.attg_d033_xsd.attg_d033 import Doc


obj = Doc(
    elem=AttRef(
        other_attributes={
            '{not-exist}bar': '123',
        }
    )
)
