from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-enumeration-1-NS"


class NistschemaSvIvListTokenEnumeration1Type(Enum):
    """
    :cvar AS_IS_TOOLS_AND_NEEDED:
    :cvar A_PARTNERSHIP_MANIPULATE_KNOWN_FOR_PROCESS_THE:
    :cvar G_REACH_AS_CONTROL_OF_HELPING_NIST_ITL:
    :cvar LAW_SIMPLEST_AND_ANY_ADOPTION_HELP_WORK_NUMBER_THE:
    :cvar TESTING_PARTNERSHIPS_THE_SOFTWARE_AUTOMATICALLY:
    :cvar THE_RESIDES_EARLY_OF_DATA_UNAMBIGUOUS:
    """
    AS_IS_TOOLS_AND_NEEDED = "as is tools and needed"
    A_PARTNERSHIP_MANIPULATE_KNOWN_FOR_PROCESS_THE = "a partnership manipulate known for process the"
    G_REACH_AS_CONTROL_OF_HELPING_NIST_ITL = "g reach as Control of helping NIST/ITL"
    LAW_SIMPLEST_AND_ANY_ADOPTION_HELP_WORK_NUMBER_THE = "law simplest and any adoption help Work number the"
    TESTING_PARTNERSHIPS_THE_SOFTWARE_AUTOMATICALLY = "testing partnerships the software automatically"
    THE_RESIDES_EARLY_OF_DATA_UNAMBIGUOUS = "the resides early of data; unambiguous"


@dataclass
class NistschemaSvIvListTokenEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-token-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-token-enumeration-1-NS"

    value: Optional[NistschemaSvIvListTokenEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
