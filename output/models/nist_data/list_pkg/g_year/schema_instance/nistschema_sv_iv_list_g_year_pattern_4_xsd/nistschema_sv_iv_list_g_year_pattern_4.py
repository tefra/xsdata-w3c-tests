from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-pattern-4-NS"


@dataclass
class NistschemaSvIvListGYearPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-pattern-4"
        namespace = "NISTSchema-SV-IV-list-gYear-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"19\d\d \d\d48 \d\d53 18\d\d \d\d43 19\d\d \d\d10 \d\d46",
            "tokens": True,
        },
    )
