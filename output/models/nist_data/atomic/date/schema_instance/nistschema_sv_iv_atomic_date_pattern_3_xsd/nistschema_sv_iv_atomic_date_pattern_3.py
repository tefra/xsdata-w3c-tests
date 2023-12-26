from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicDatePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-date-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d\d90-\d7-2\d",
        },
    )
