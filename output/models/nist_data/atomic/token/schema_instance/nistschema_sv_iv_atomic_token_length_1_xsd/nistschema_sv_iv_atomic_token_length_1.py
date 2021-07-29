from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-length-1-NS"


@dataclass
class NistschemaSvIvAtomicTokenLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-length-1"
        namespace = "NISTSchema-SV-IV-atomic-token-length-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 0,
        }
    )
