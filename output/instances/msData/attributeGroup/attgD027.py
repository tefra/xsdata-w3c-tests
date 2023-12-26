from output.models.ms_data.attribute_group.attg_d027_xsd.attg_d027 import AttRef
from output.models.ms_data.attribute_group.attg_d027_xsd.attg_d027 import Doc


obj = Doc(
    elem=AttRef(
        foo=123,
        foo_attributes={
            '{foo}a': 'b',
        }
    )
)
