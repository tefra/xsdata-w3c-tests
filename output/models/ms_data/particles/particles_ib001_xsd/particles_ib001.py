from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar foo_or_foo1:
    """
    class Meta:
        name = "base"

    foo_or_foo1: List[object] = field(
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
        }
    )


@dataclass
class Doc(Base):
    """
    :ivar foo:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo: List[bool] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        }
    )
