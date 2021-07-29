from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-minLength-2-NS"


@dataclass
class NistschemaSvIvAtomicNameMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-Name-minLength-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 63,
        }
    )
