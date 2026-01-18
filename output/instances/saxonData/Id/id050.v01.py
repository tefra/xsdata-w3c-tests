from output.models.saxon_data.id.id051_xsd.id051 import Doc
from output.models.saxon_data.id.id051_xsd.id051 import EmpType


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
