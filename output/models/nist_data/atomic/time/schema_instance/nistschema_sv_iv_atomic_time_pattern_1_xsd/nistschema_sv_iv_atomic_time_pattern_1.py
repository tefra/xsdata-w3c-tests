from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicTimePattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-time-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d9:\d2:5\d",
        },
    )
