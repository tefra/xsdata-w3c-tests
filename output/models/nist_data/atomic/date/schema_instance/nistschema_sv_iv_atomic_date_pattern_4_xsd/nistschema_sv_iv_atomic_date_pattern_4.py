from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicDatePattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-date-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"17\d\d-\d0-1\d",
        },
    )
