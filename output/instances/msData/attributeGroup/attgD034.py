from output.models.ms_data.attribute_group.attg_d034_xsd.attg_d034 import AttRef
from output.models.ms_data.attribute_group.attg_d034_xsd.attg_d034 import Doc


obj = Doc(
    elem=AttRef(
        foo=None,
        other_attributes={
            "{http://foo}att": "123",
        }
    )
)