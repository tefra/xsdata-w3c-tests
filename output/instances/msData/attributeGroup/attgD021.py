from output.models.ms_data.attribute_group.attg_d021_xsd.attg_d021 import AttgRef
from output.models.ms_data.attribute_group.attg_d021_xsd.attg_d021 import Doc


obj = Doc(
    elem=[
        AttgRef(
            att1=123,
            any_attributes={
                '{foo}foo': 'foo',
            }
        ),
    ]
)
