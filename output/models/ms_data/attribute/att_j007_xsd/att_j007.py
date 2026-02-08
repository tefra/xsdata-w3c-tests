from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class AttRef:
    class Meta:
        name = "attRef"

    att1: object = field(
        metadata={
            "type": "Attribute",
        }
    )
    att2: object = field(
        metadata={
            "type": "Attribute",
        }
    )
    bar: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
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
    x1: object = field(
        metadata={
            "type": "Attribute",
        }
    )
    x2: object = field(
        metadata={
            "type": "Attribute",
        }
    )
    foo: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
