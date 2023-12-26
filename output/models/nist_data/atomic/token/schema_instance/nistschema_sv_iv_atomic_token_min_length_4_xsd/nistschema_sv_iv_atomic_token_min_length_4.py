from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-minLength-4-NS"


@dataclass
class NistschemaSvIvAtomicTokenMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-token-minLength-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 202,
        },
    )
