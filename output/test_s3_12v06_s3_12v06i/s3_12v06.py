from output.models.ibm_data.valid.s3_12.s3_12v06_xsd.s3_12v06 import ChildTypeBase
from output.models.ibm_data.valid.s3_12.s3_12v06_xsd.s3_12v06 import CtBase
from output.models.ibm_data.valid.s3_12.s3_12v06_xsd.s3_12v06 import Root


obj = Root(
    person=[
        CtBase(
            child=[
                ChildTypeBase(
                    name='C1',
                    dob='2007-10-10'
                ),
                ChildTypeBase(
                    name='C2',
                    dob='2003-01-02'
                ),
            ],
            number_of_children=2
        ),
        CtBase(
            child=[
                ChildTypeBase(
                    name='C1',
                    dob='2000-01-01'
                ),
            ],
            number_of_children=7
        ),
        CtBase(
            number_of_children=-5
        ),
    ]
)
