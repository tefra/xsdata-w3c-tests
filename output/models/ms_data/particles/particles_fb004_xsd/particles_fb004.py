from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    g1_or_g2: None | Base.G1 | Base.G2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g1",
                    "type": ForwardRef("Base.G1"),
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "g2",
                    "type": ForwardRef("Base.G2"),
                    "namespace": "http://xsdtesting",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class G1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
            },
        )

    @dataclass(kw_only=True)
    class G2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
            },
        )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    s1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    s2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
