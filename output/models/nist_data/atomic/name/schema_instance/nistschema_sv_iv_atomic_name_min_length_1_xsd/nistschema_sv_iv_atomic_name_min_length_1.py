from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-minLength-1-NS"


@dataclass
class NistschemaSvIvAtomicNameMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-minLength-1"
        namespace = "NISTSchema-SV-IV-atomic-Name-minLength-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )
