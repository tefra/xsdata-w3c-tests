from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d\d55-0\d-\d8T\d6:1\d:0\d",
        }
    )
