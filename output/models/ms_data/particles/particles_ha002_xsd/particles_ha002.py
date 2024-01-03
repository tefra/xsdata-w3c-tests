from dataclasses import dataclass, field
from typing import Optional, Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )
    e2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
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
