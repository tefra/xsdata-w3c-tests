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
    documentation documentation bar.
    """

    class Meta:
        name = "base"

    e1_or_e2: None | A | object = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": A,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "e2",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
