from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicDatePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-date-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d\d10-\d4-1\d",
        }
    )
