from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    g1_or_g2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g1",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "g2",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
            "max_occurs": 2,
        }
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    s1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    s2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
