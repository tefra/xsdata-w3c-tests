from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicDurationPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"P\d\d76Y\d4M2\dDT1\dH\d9M\d9S",
        },
    )
