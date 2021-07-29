from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9A-F]{18}",
        }
    )
