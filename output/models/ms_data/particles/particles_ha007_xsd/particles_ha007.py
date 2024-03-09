from dataclasses import dataclass, field
from typing import Any, List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    e3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequence": 1,
        },
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e2: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    e3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
