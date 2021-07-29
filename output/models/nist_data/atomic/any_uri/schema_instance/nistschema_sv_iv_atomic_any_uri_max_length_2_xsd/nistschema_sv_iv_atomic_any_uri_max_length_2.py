from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-maxLength-2-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-maxLength-2"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-maxLength-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 40,
        }
    )
