from output.models.ms_data.attribute_group.attg_d031_xsd.attg_d031 import AttRef
from output.models.ms_data.attribute_group.attg_d031_xsd.attg_d031 import Doc


obj = Doc(
    elem=AttRef(
        foo=123,
        other_attributes={
            '{notExist}b': '123',
        }
    )
)
