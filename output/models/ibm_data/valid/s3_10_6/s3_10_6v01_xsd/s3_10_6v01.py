from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"

    e1: T.E1 = field(
        metadata={
            "type": "Element",
            "namespace": "a",
        }
    )
    e2: T.E2 = field(
        metadata={
            "type": "Element",
            "namespace": "a",
        }
    )

    @dataclass(kw_only=True)
    class E1:
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class E2:
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
