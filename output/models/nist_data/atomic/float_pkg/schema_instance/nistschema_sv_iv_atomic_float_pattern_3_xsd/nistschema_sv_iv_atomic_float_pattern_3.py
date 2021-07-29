from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicFloatPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-float-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{1}\.\d{2}E\d{1}",
        }
    )
