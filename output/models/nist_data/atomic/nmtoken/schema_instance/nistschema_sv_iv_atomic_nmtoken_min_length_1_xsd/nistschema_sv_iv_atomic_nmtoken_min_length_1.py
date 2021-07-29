from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-1-NS"


@dataclass
class NistschemaSvIvAtomicNmtokenMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-1"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
