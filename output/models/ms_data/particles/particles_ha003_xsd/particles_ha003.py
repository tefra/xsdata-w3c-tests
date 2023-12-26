from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    e1_or_e2_or_e3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
                {
                    "name": "e3",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
            "max_occurs": 2,
        },
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
