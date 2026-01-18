from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class AttRef:
    class Meta:
        name = "attRef"

    att1: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    att2: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: None | AttRef = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    foo: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
