from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{1}",
        },
    )
