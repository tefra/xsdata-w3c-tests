from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{9}",
        },
    )
