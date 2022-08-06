from output.models.ms_data.attribute_group.attg_d020_xsd.attg_d020 import Doc


obj = Doc(
    att1=None,
    abc=None,
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://xsdtesting attgD020.xsd",
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "attgD020a.xsd",
        "foo": "bar",
    },
    content=[
        "&#10;&#9;&#9;&#10;&#9;&#9;testing&#10;&#9;&#9;&#10;",
    ]
)
