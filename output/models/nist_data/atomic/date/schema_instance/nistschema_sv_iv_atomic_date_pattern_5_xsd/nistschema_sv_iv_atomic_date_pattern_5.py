from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicDatePattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-date-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d\d44-\d2-\d5",
        },
    )
