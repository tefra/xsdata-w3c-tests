from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicFloatPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-float-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{1}\.\d{7}E\-\d{2}",
        }
    )
