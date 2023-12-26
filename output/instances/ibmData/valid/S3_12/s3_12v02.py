from output.models.ibm_data.valid.s3_12.s3_12v02_xsd.s3_12v02 import MixedTitleType
from output.models.ibm_data.valid.s3_12.s3_12v02_xsd.s3_12v02 import Root


obj = Root(
    title=[
        MixedTitleType(
            type_value='text',
            content=[
                'My News',
            ]
        ),
        MixedTitleType(
            type_value='number',
            content=[
                '122323',
            ]
        ),
        MixedTitleType(
            type_value='mixed',
            content=[
                'D413',
            ]
        ),
        MixedTitleType(
            content=[
                'My News',
            ]
        ),
    ]
)
