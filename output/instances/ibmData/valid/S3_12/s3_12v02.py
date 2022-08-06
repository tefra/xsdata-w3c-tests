from output.models.ibm_data.valid.s3_12.s3_12v02_xsd.s3_12v02 import MixedTitleType
from output.models.ibm_data.valid.s3_12.s3_12v02_xsd.s3_12v02 import Root


obj = Root(
    title=[
        MixedTitleType(
            type="text",
            content=[
                "My News",
            ],
            value=""
        ),
        MixedTitleType(
            type="number",
            content=[
                "122323",
            ],
            value=""
        ),
        MixedTitleType(
            type="mixed",
            content=[
                "D413",
            ],
            value=""
        ),
        MixedTitleType(
            type=None,
            content=[
                "My News",
            ],
            value=""
        ),
    ]
)
