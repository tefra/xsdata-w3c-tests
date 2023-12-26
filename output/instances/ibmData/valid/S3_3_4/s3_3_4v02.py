from output.models.ibm_data.valid.s3_3_4.s3_3_4v02_xsd.s3_3_4v02 import AnyAttr
from output.models.ibm_data.valid.s3_3_4.s3_3_4v02_xsd.s3_3_4v02 import Root


obj = Root(
    a=AnyAttr(
        id1='qwe',
        any_attributes={
            'globalAttr': 'asd',
        }
    )
)
