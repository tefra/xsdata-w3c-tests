from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-maxLength-4-NS"


@dataclass
class NistschemaSvIvAtomicTokenMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-token-maxLength-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 670,
        }
    )
