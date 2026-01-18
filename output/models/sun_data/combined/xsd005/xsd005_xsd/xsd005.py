from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    a: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    b: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    c: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )


@dataclass(kw_only=True)
class Ext(Base):
    class Meta:
        name = "ext"

    d: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    e: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
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
