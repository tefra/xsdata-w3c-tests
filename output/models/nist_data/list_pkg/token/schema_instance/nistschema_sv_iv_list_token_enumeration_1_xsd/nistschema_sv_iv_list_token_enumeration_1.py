from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-enumeration-1-NS"


class NistschemaSvIvListTokenEnumeration1Type(Enum):
    THE_RESIDES_EARLY_OF_DATA_UNAMBIGUOUS = (
            "the",
            "resides",
            "early",
            "of",
            "data;",
            "unambiguous",
        )
    TESTING_PARTNERSHIPS_THE_SOFTWARE_AUTOMATICALLY = (
            "testing",
            "partnerships",
            "the",
            "software",
            "automatically",
        )
    G_REACH_AS_CONTROL_OF_HELPING_NIST_ITL = (
            "g",
            "reach",
            "as",
            "Control",
            "of",
            "helping",
            "NIST/ITL",
        )
    LAW_SIMPLEST_AND_ANY_ADOPTION_HELP_WORK_NUMBER_THE = (
            "law",
            "simplest",
            "and",
            "any",
            "adoption",
            "help",
            "Work",
            "number",
            "the",
        )
    AS_IS_TOOLS_AND_NEEDED = (
            "as",
            "is",
            "tools",
            "and",
            "needed",
        )
    A_PARTNERSHIP_MANIPULATE_KNOWN_FOR_PROCESS_THE = (
            "a",
            "partnership",
            "manipulate",
            "known",
            "for",
            "process",
            "the",
        )


@dataclass
class NistschemaSvIvListTokenEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-token-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-token-enumeration-1-NS"

    value: Optional[NistschemaSvIvListTokenEnumeration1Type] = field(
        default=None
    )
