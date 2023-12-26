from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{10}",
        },
    )
