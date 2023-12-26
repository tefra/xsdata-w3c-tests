from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"19\d\d-0\d-0\dT\d5:1\d:3\d",
        },
    )
