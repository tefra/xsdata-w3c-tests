from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9A-F]{66}",
        }
    )
