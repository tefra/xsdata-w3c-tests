from dataclasses import dataclass, field

from output.models.saxon_data.override.over002_xsd.over002 import Para


@dataclass
class Doc:
    class Meta:
        name = "doc"

    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
