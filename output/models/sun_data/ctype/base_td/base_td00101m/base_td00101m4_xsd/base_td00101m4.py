from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "baseTD"


@dataclass
class Test:
    abc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Test1:
    abc: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )


@dataclass
class Root(Test):
    class Meta:
        name = "root"
        namespace = "baseTD"
