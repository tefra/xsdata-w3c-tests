from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    e2: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    e3: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "max_occurs": 2,
            "sequence": 1,
        },
    )


@dataclass(kw_only=True)
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    e3: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
