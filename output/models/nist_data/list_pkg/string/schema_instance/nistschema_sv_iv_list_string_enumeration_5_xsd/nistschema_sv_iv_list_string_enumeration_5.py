from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-enumeration-5-NS"


class NistschemaSvIvListStringEnumeration5Type(Enum):
    PROVIDES_PROVIDE_HIGHLY_INDUSTRY_ANY_ON_TOOLS_WITH_FOR = (
        "provides",
        "Provide",
        "highly",
        "industry",
        "any",
        "on",
        "tools",
        "with",
        "for",
    )
    TO_E_XTENSIBLE_CAN_IS_INFORMATION_ASPECTS_STANDARD = (
        "to",
        "eXtensible",
        "can",
        "is",
        "information",
        "aspects",
        "standard",
    )
    TEST_FURTHERMORE_AND_DOCUMENTS_AS_BE = (
        "test",
        "Furthermore",
        "and",
        "documents",
        "as",
        "be",
    )
    CAN_NSRL_PROMISES_DATA_XML_ACTING = (
        "can",
        "NSRL",
        "promises",
        "data;",
        "XML",
        "acting",
    )
    BECOME_TO_XML_THAT_WILL_THE_PICO_CELLULAR_CROSS_OVER_MARKET_IMPACT = (
        "become",
        "to",
        "XML",
        "that",
        "will",
        "the",
        "pico-cellular",
        "cross-over",
        "market",
        "impact",
    )
    SPECIFICATIONS_BUILD_FOR_THE_WILL_WEB = (
        "specifications",
        "build",
        "for",
        "the",
        "will",
        "web",
    )


@dataclass(kw_only=True)
class NistschemaSvIvListStringEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-string-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-string-enumeration-5-NS"

    value: NistschemaSvIvListStringEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
