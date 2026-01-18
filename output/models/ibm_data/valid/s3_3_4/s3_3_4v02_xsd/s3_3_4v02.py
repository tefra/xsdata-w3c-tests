from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class AnyAttr:
    class Meta:
        name = "anyAttr"

    id1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    a: AnyAttr = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
