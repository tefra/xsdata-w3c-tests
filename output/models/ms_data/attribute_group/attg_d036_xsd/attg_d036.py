from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class AttRef:
    class Meta:
        name = "attRef"

    att: int = field(
        init=False,
        default=37,
        metadata={
            "type": "Attribute",
        },
    )
    att1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | AttRef = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
