from dataclasses import dataclass, field

from output.models.saxon_data.override.over012_xsd.over012 import (
    StructuredDate,
)


@dataclass
class Doc:
    class Meta:
        name = "doc"

    para: list[StructuredDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
