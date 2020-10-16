from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"a{0,1}b{1,2}c{2,3}",
        }
    )
