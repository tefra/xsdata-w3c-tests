from output.models.ms_data.attribute_group.attg_d029_xsd.attg_d029 import AttRef
from output.models.ms_data.attribute_group.attg_d029_xsd.attg_d029 import Doc


obj = Doc(
    elem=AttRef(
        foo=123,
        target_namespace_attributes={
            '{http://xsdtesting}bar': '123',
        }
    )
)
