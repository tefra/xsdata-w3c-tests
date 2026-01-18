from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "attrWildcard"


@dataclass(kw_only=True)
class A1:
    class Meta:
        name = "A"

    b: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class A(A1):
    class Meta:
        name = "a"
        namespace = "attrWildcard"
