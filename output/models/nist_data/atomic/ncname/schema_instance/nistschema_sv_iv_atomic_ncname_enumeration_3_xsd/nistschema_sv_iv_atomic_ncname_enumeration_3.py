from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-enumeration-3-NS"


class NistschemaSvIvAtomicNcnameEnumeration3Type(Enum):
    """
    :cvar VALUE_REPOSITORY_HAVING_BASED_ENTERPRISES_CONTRIBUTE_FILTE:
    :cvar COF_ISSUES_INCLUDES_USED_20_THE_E_WE_TO_MANUAL_TO:
    :cvar CUSED_DE:
    :cvar GTOOLS_THE_THE_ARE_KEY_MECHANISM_THE_I:
    :cvar UPROFILES_PA:
    :cvar YBOTH_IN_EACH_THE_DISCUSS_ELECTRONIC_CAN_I:
    """
    VALUE_REPOSITORY_HAVING_BASED_ENTERPRISES_CONTRIBUTE_FILTE = "_repository_having-based-enterprises_contribute_filte"
    COF_ISSUES_INCLUDES_USED_20_THE_E_WE_TO_MANUAL_TO = "cof.issues.includes.used-20_the.e-we.to.manual-to-"
    CUSED_DE = "cused.de"
    GTOOLS_THE_THE_ARE_KEY_MECHANISM_THE_I = "gtools_the-the-are.key_mechanism_the_i"
    UPROFILES_PA = "uprofiles.pa"
    YBOTH_IN_EACH_THE_DISCUSS_ELECTRONIC_CAN_I = "yboth-in-each-the_discuss_electronic_can_i"


@dataclass
class NistschemaSvIvAtomicNcnameEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-NCName-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicNcnameEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )