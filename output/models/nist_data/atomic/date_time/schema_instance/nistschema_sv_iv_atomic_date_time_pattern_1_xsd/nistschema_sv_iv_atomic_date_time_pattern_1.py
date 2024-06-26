from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicDateTimePattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"19\d\d-0\d-\d8T\d8:\d5:5\d",
        },
    )
