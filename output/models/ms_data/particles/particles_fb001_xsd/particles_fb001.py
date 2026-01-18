from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    c1_or_c2: None | Base.C1 | Base.C2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": ForwardRef("Base.C1"),
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "c2",
                    "type": ForwardRef("Base.C2"),
                    "namespace": "http://xsdtesting",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class C1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
            },
        )

    @dataclass(kw_only=True)
    class C2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
            },
        )


@dataclass(kw_only=True)
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    g1_or_g2: None | Doc.G1 | Doc.G2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g1",
                    "type": ForwardRef("Doc.G1"),
                },
                {
                    "name": "g2",
                    "type": ForwardRef("Doc.G2"),
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
            },
        )

    @dataclass(kw_only=True)
    class G2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )
