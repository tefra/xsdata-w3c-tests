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
            "required": True,
        }
    )
    e2: T.E2 = field(
        metadata={
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    e3: T.E3 = field(
        metadata={
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    e4: T.E4 = field(
        metadata={
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class E1:
        other_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            },
        )

    @dataclass(kw_only=True)
    class E2:
        target_namespace_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##targetNamespace",
            },
        )

    @dataclass(kw_only=True)
    class E3:
        local_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##local",
            },
        )

    @dataclass(kw_only=True)
    class E4:
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
