from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicDecimalPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\-\d{2}\.\d{3}",
        }
    )
