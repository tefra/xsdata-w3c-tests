from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: list[float | bytes | int | QName] = field(
        init=False,
        default_factory=lambda: [
            12,
            QName("abcdef"),
            4.0,
            QName("{a}a"),
            QName("{a}b"),
            QName("{b}a"),
            QName("{b}b"),
        ],
        metadata={
            "tokens": True,
        },
    )
