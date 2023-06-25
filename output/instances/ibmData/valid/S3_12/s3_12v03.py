from output.models.ibm_data.valid.s3_12.s3_12v03_xsd.s3_12v03 import Root


obj = Root(
    title=[
        Root.TypeText(
            type_value="text",
            content=[
                "My News",
            ]
        ),
        Root.TypeText(
            type_value="number",
            content=[
                "122323",
            ]
        ),
    ]
)
