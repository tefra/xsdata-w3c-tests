from dataclasses import dataclass, field
from typing import Any, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    e: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )
    f: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )


@dataclass
class Base:
    class Meta:
        name = "base"

    e: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )
    f: Optional[object] = field(
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

    e: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    f: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Test(B):
    class Meta:
        name = "test"

    e: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    f: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
