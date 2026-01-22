from output.models.saxon_data.id.id052_xsd.id052 import Doc
from output.models.saxon_data.id.id052_xsd.id052 import EmpType


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
