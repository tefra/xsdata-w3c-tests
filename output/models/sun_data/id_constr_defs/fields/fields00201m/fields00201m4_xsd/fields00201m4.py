from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "IdConstrDefs/fields"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "IdConstrDefs/fields"

    number: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
