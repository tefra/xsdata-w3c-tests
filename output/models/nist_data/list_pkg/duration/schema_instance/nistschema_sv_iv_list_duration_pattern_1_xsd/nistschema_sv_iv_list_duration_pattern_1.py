from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDurationPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-pattern-1"
        namespace = "NISTSchema-SV-IV-list-duration-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"P\d\d75Y\d3M\d9DT0\dH\d2M3\dS P19\d\dY0\dM1\dDT0\dH1\dM\d1S P19\d\dY\d3M2\dDT\d4H\d7M\d7S P\d\d86Y\d9M\d5DT\d6H4\dM\d9S P19\d\dY\d2M\d2DT\d9H3\dM0\dS P\d\d90Y0\dM2\dDT\d7H2\dM0\dS P\d\d94Y\d0M1\dDT0\dH1\dM4\dS P\d\d71Y0\dM\d1DT\d3H\d7M4\dS",
            "tokens": True,
        },
    )
