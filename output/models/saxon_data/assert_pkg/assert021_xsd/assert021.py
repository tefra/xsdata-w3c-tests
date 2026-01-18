from __future__ import annotations

from dataclasses import dataclass, field

from output.models.saxon_data.assert_pkg.assert021_xsd.assert021a import Temp

__NAMESPACE__ = "http://assert021.ns/"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://assert021.ns/"

    temp: list[Temp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
