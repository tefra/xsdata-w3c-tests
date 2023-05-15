from decimal import Decimal
from output.models.saxon_data.override.over008_xsd.over008 import Section


obj = Section(
    head="Intro",
    section=[
        Section(
            head="Bumph",
            id="b",
            nr=Decimal("1.1")
        ),
        Section(
            head="More Bumph",
            id="c",
            other_attributes={
                "{http://www.w3.org/XML/1998/namespace}space": "preserve",
            },
            nr=Decimal("1.2")
        ),
    ],
    id="a",
    nr=Decimal("1")
)
