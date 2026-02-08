from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.simple_type.test298668_a_xsd.test298668_b import (
    TPredefinedLnclassEnum,
)

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    value: str | TPredefinedLnclassEnum = field(
        default="",
        metadata={
            "pattern": r"\p{Lu}+",
        },
    )
