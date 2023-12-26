from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicBooleanPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-boolean-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[1]{1}",
        },
    )
