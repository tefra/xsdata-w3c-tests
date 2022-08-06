from output.models.ibm_data.valid.d4_3_15.d4_3_15v03_xsd.d4_3_15v03 import Data
from output.models.ibm_data.valid.d4_3_15.d4_3_15v03_xsd.d4_3_15v03 import ParentType
from output.models.ibm_data.valid.d4_3_15.d4_3_15v03_xsd.d4_3_15v03 import TimerType
from xsdata.models.datatype import XmlDate


obj = Data(
    timer=[
        TimerType(
            time=30,
            iterations=None
        ),
        TimerType(
            time=None,
            iterations=15
        ),
    ],
    parent=[
        ParentType(
            child=None,
            grandchild=ParentType.Grandchild(
                name="abc",
                dob=XmlDate(2007, 1, 1)
            )
        ),
        ParentType(
            child=ParentType.Child(
                name="abc",
                dob=XmlDate(1997, 1, 1)
            ),
            grandchild=None
        ),
    ]
)
