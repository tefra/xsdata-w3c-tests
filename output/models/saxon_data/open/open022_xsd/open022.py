from dataclasses import dataclass, field
from typing import List


@dataclass
class B:
    open_com_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
        }
    )


@dataclass
class R(B):
    pass


@dataclass
class Doc(R):
    class Meta:
        name = "doc"
