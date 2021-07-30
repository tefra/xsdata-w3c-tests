from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-pattern-3-NS"


@dataclass
class NistschemaSvIvUnionShortGYearPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-pattern-3"
        namespace = "NISTSchema-SV-IV-union-short-gYear-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d\d50",
        }
    )
