from dataclasses import dataclass, field
from typing import List, Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    foo_or_foo1: List[bool] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": bool,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "foo1",
                    "type": bool,
                    "namespace": "http://xsdtesting",
                },
            ),
            "max_occurs": 6,
        },
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo1: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
