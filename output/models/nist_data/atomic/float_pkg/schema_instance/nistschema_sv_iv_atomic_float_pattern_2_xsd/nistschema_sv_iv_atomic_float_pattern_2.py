from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicFloatPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-float-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{2}E\-\d{1}",
        }
    )
