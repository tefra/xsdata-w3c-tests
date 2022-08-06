from decimal import Decimal
from output.models.saxon_data.override.over008_xsd.over008 import Section


obj = Section(
    head="Intro",
    section=[
        Section(
            head="Bumph",
            section=[],
            id="b",
            other_attributes={},
            nr=Decimal("1.1")
        ),
        Section(
            head="More Bumph",
            section=[],
            id="c",
            other_attributes={
                "{http://www.w3.org/XML/1998/namespace}space": "preserve",
            },
            nr=Decimal("1.2")
        ),
    ],
    id="a",
    other_attributes={},
    nr=Decimal("1")
)
