from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-3-NS"


@dataclass
class NistschemaSvIvAtomicNmtokenMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-3"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 35,
        },
    )
