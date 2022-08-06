from output.models.ms_data.attribute_group.attg_d022_xsd.attg_d022 import Doc


obj = Doc(
    att1=None,
    foo=None,
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "attgD022.xsd",
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "a attgD022a.xsd",
        "{a}a": "b",
    },
    content=[
        "&#10;testing&#10;",
    ]
)
