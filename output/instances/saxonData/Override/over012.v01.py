from output.models.saxon_data.override.over012_xsd.over012 import StructuredDate
from output.models.saxon_data.override.over012_xsd.over012a import Doc


obj = Doc(
    para=[
        StructuredDate(
            year=2010,
            month=5,
            day=11
        ),
    ]
)
