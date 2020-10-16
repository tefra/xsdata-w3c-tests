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
            "pattern": r"---([123]0)|([12]?[1-9])|(31)",
        }
    )
