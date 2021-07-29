from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"--0\d-\d8",
        }
    )
