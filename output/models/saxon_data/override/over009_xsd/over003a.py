from __future__ import annotations

from dataclasses import dataclass, field

from output.models.saxon_data.override.over009_xsd.over003 import Para


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
