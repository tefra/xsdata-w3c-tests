from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicIntPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-int-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\-\d{5}",
        },
    )
