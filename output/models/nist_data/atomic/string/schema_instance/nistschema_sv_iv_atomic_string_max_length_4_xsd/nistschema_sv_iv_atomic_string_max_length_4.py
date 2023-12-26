from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-maxLength-4-NS"


@dataclass
class NistschemaSvIvAtomicStringMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-string-maxLength-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 205,
        },
    )
