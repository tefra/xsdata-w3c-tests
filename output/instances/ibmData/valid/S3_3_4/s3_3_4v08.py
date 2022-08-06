from output.models.ibm_data.valid.s3_3_4.s3_3_4v08_xsd.s3_3_4v08 import Idrefs
from output.models.ibm_data.valid.s3_3_4.s3_3_4v08_xsd.s3_3_4v08 import Ids
from output.models.ibm_data.valid.s3_3_4.s3_3_4v08_xsd.s3_3_4v08 import Root
from output.models.ibm_data.valid.s3_3_4.s3_3_4v08_xsd.s3_3_4v08 import ValueConstraint


obj = Root(
    a=Ids(
        id="asd"
    ),
    b=Idrefs(
        idref=ValueConstraint.ASD
    )
)
