from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicIntegerPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-integer-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{5}",
        },
    )
