from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class AttRef:
    class Meta:
        name = "attRef"

    foo: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: None | object = field(
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
