from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "urn:foo"


@dataclass
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


@dataclass
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


@dataclass
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


@dataclass
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
