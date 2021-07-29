from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicTimePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-time-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d6:\d9:\d9",
        }
    )
