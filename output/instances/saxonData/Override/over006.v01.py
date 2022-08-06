from decimal import Decimal
from output.models.saxon_data.override.over006_xsd.over006 import Section


obj = Section(
    head="Intro",
    section=[
        Section(
            head="Bumph",
            section=[],
            nr=Decimal("1.1")
        ),
        Section(
            head="More Bumph",
            section=[],
            nr=Decimal("1.2")
        ),
    ],
    nr=Decimal("1")
)
