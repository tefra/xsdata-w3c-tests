from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9A-F]{46}",
        },
    )
