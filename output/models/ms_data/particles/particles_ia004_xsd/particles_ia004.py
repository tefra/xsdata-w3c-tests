from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    e1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "min_occurs": 2,
            "max_occurs": 6,
        },
    )
    e2: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "min_occurs": 2,
            "max_occurs": 6,
        },
    )


@dataclass(kw_only=True)
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
