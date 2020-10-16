from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Root:
    """
    :ivar union_of_ids:
    :ivar idref:
    """
    class Meta:
        name = "root"

    union_of_ids: List[Union[int, bool, str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    idref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
