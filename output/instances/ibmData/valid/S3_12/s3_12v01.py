from output.models.ibm_data.valid.s3_12.s3_12v01_xsd.s3_12v01 import Root
from output.models.ibm_data.valid.s3_12.s3_12v01_xsd.s3_12v01 import StringTitleType


obj = Root(
    title=[
        StringTitleType(
            type_value="text",
            content=[
                "My News",
            ]
        ),
        StringTitleType(
            type_value="number",
            content=[
                "122323",
            ]
        ),
        StringTitleType(
            type_value="mixed",
            content=[
                "D413",
            ]
        ),
        StringTitleType(
            content=[
                "My News",
            ]
        ),
    ]
)
