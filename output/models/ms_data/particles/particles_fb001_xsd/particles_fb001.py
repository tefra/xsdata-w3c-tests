from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    c1_or_c2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "c2",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
        }
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    g1_or_g2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g1",
                    "type": object,
                },
                {
                    "name": "g2",
                    "type": object,
                },
            ),
            "max_occurs": 2,
        }
    )
