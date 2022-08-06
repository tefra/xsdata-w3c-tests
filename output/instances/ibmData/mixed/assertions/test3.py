from output.models.ibm_data.mixed.assertions.test3_xsd.test3 import Data
from output.models.ibm_data.mixed.assertions.test3_xsd.test3 import ParentType
from output.models.ibm_data.mixed.assertions.test3_xsd.test3 import TimerType
from xsdata.models.datatype import XmlDate


obj = Data(
    timer=TimerType(
        time=30,
        iterations=None
    ),
    parent=ParentType(
        child=ParentType.Child(
            name="abc",
            dob=XmlDate(1997, 1, 1)
        ),
        grandchild=None
    )
)
