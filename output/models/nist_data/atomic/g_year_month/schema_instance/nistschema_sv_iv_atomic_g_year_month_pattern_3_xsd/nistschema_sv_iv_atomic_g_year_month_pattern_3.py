from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d\d76-0\d",
        }
    )
