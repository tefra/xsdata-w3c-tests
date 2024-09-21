from output.models.saxon_data.id.id050_xsd.id050 import Doc
from output.models.saxon_data.id.id050_xsd.id050 import EmpType


obj = Doc(
    emp=[
        EmpType(
            name='John',
            nr=23
        ),
        EmpType(
            name='Mary',
            nr=29
        ),
        EmpType(
            name='Ahmed',
            nr=42
        ),
    ]
)
