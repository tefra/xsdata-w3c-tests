from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    e: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )
    f: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    e: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )
    f: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )


@dataclass(kw_only=True)
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    f: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Test(B):
    class Meta:
        name = "test"

    e: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    f: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
