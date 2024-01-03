from output.models.ibm_data.valid.s3_12.s3_12v01_xsd.s3_12v01 import Root
from output.models.ibm_data.valid.s3_12.s3_12v01_xsd.s3_12v01 import TitleType


obj = Root(
    title=[
        TitleType(
            type_value='text',
            content=[
                'My News',
            ]
        ),
        TitleType(
            type_value='number',
            content=[
                '122323',
            ]
        ),
        TitleType(
            type_value='mixed',
            content=[
                'D413',
            ]
        ),
        TitleType(
            content=[
                'My News',
            ]
        ),
    ]
)
