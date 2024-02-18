from dataclasses import dataclass, field
from typing import List
from output.models.saxon_data.override.over009_xsd.over003 import Para


@dataclass
class Doc:
    class Meta:
        name = "doc"

    para: List[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
