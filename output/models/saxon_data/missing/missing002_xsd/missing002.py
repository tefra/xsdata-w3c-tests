from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Bad:
    class Meta:
        name = "bad"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Good:
    class Meta:
        name = "good"

    value: int = field()


@dataclass(kw_only=True)
class Perfect:
    class Meta:
        name = "perfect"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
