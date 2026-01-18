from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class B:
    open_com_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
        },
    )


@dataclass(kw_only=True)
class R(B):
    pass


@dataclass(kw_only=True)
class Doc(R):
    class Meta:
        name = "doc"
