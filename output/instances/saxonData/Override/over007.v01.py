from decimal import Decimal
from output.models.saxon_data.override.over007_xsd.over007 import Section


obj = Section(
    head="Intro",
    section=[
        Section(
            head="Bumph",
            nr=Decimal("1.1")
        ),
        Section(
            head="More Bumph",
            nr=Decimal("1.2")
        ),
    ],
    nr=Decimal("1")
)
