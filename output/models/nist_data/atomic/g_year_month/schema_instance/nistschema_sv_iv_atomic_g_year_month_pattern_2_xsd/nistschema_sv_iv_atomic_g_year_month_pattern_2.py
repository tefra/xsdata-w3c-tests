from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d\d31-\d3",
        }
    )
