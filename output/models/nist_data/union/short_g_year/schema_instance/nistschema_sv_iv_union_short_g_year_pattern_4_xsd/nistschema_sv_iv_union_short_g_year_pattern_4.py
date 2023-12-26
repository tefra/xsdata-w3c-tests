from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-pattern-4-NS"


@dataclass
class NistschemaSvIvUnionShortGYearPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-pattern-4"
        namespace = "NISTSchema-SV-IV-union-short-gYear-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{2}",
        },
    )
