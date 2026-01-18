from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Uid:
    class Meta:
        name = "uid"
        nillable = True

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    uid: list[Uid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "nillable": True,
        },
    )
