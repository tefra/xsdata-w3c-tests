from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-whiteSpace-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "replace",
        },
    )
