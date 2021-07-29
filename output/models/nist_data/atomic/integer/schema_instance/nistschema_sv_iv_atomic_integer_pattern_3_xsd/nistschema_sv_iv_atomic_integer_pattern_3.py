from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicIntegerPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\-\d{1}",
        }
    )
