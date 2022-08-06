from output.models.ibm_data.valid.s3_12.s3_12v01_xsd.s3_12v01 import Root
from output.models.ibm_data.valid.s3_12.s3_12v01_xsd.s3_12v01 import StringTitleType


obj = Root(
    title=[
        StringTitleType(
            type="text",
            content=[
                "My News",
            ],
            value=""
        ),
        StringTitleType(
            type="number",
            content=[
                "122323",
            ],
            value=""
        ),
        StringTitleType(
            type="mixed",
            content=[
                "D413",
            ],
            value=""
        ),
        StringTitleType(
            type=None,
            content=[
                "My News",
            ],
            value=""
        ),
    ]
)
