from dataclasses import dataclass, field
from typing import Optional, Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    e0_or_e1_or_e2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e0",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "e1",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "e2",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
        },
    )


@dataclass
class Testing(Base):
    class Meta:
        name = "testing"

    e0: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
