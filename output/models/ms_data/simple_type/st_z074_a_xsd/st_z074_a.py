from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.simple_type.st_z074_a_xsd.st_z074_b import List2

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    value: list[str | List2] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
