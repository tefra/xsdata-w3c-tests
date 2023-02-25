from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    e2_or_e3_or_e4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e2",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "e3",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "e4",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
        }
    )


@dataclass
class Testing(Base):
    class Meta:
        name = "testing"


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
