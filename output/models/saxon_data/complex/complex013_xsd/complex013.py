from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    """
    :ivar e:
    """
    class Meta:
        name = "root"
        nillable = True

    e: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
