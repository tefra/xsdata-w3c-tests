from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "urn:foo"


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    a_b_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "urn:a urn:b",
        },
    )


@dataclass(kw_only=True)
class Alias(Base):
    class Meta:
        name = "alias"
        namespace = "urn:foo"

    a_b_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Extension(Base):
    class Meta:
        name = "extension"
        namespace = "urn:foo"

    c_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "urn:c",
        },
    )


@dataclass(kw_only=True)
class Restriction(Base):
    class Meta:
        name = "restriction"
        namespace = "urn:foo"

    a_b_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    a_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "urn:a",
        },
    )
