from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-zA-Z0-9+/]{68}",
        },
    )
