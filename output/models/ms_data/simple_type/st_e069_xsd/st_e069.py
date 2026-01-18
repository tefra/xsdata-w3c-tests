from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: list[XmlPeriod | str | int] = field(
        init=False,
        default_factory=lambda: [
            "a",
            "b",
        ],
        metadata={
            "tokens": True,
        },
    )
