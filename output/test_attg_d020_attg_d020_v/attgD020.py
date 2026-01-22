from output.models.ms_data.attribute_group.attg_d020_xsd.attg_d020 import Doc


obj = Doc(
    any_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': 'http://xsdtesting attgD020.xsd',
        '{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'attgD020a.xsd',
        'foo': 'bar',
    },
    content=[
        '\n\t\t\n\t\ttesting\n\t\t\n',
    ]
)
