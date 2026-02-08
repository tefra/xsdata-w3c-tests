from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class A:
    a: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )


@dataclass(kw_only=True)
class B:
    b: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )


@dataclass(kw_only=True)
class Base:
    """
    documentation documentation.
    """

    class Meta:
        name = "base"

    e1: A = field(
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )
    e2: None | object = field(
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
