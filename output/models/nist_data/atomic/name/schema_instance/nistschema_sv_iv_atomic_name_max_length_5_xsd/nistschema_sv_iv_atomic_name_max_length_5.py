from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-maxLength-5-NS"


@dataclass
class NistschemaSvIvAtomicNameMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-maxLength-5"
        namespace = "NISTSchema-SV-IV-atomic-Name-maxLength-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        },
    )
