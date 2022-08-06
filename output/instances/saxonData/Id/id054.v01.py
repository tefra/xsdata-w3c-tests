from output.models.saxon_data.id.id054_xsd.id054 import Doc
from output.models.saxon_data.id.id054_xsd.id054 import EmpType


obj = Doc(
    emp=[
        EmpType(
            name="John",
            nr=23,
            manager=None
        ),
        EmpType(
            name="Mary",
            nr=29,
            manager=None
        ),
        EmpType(
            name="Ahmed",
            nr=42,
            manager=29
        ),
    ]
)
