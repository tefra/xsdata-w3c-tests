from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.identity_constraint.id_g018_xsd.id_g018a import R


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"

    r: None | R = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "importNS",
        },
    )
    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    t: list[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
