from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicGMonthPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"--1\d",
        }
    )
