from dataclasses import dataclass, field
from typing import Any, Optional

__NAMESPACE__ = "foo"


@dataclass
class Base:
    class Meta:
        name = "base"

    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    c: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )


@dataclass
class Ext(Base):
    class Meta:
        name = "ext"

    d: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    e: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    item: list[Base] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Rst(Base):
    class Meta:
        name = "rst"

    b: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
