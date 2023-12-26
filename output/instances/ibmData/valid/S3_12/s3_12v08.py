from output.models.ibm_data.valid.s3_12.s3_12v08_xsd.s3_12v08 import ChildType
from output.models.ibm_data.valid.s3_12.s3_12v08_xsd.s3_12v08 import Root


obj = Root(
    child=[
        ChildType(
            type1=True,
            content=[
                'true',
            ]
        ),
        ChildType(
            type2=True,
            content=[
                '1234',
            ]
        ),
        ChildType(
            content=[
                'childType',
            ]
        ),
        ChildType(
            type1=True,
            type2=False,
            content=[
                'childType',
            ]
        ),
    ]
)
