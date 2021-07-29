from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicBooleanPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-boolean-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[1]{1}",
        }
    )
