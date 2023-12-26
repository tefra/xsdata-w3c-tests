from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    union_of_ids: List[Union[int, str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
