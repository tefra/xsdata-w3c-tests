from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicLongPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-long-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\-\d{18}",
        },
    )
