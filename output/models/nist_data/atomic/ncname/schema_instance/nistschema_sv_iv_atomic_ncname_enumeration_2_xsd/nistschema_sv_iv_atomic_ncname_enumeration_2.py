from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-enumeration-2-NS"


class NistschemaSvIvAtomicNcnameEnumeration2Type(Enum):
    """
    :cvar OSOFTWARE_WIDESPREAD_MUST_RE:
    :cvar VTO_SIGNIFICANT_GOVERNMENT_DISSEMINATE_INDUSTRY_A_OVER:
    :cvar INDUSTRY_THE_IN_SPECIFICATIONS_THE_D:
    :cvar HSYSTEMS_I:
    :cvar BRESOURCE_AND_C:
    :cvar FBOTH_TH:
    :cvar INVESTIGATION_OF_HELP_ITS_BE_SUPPORT_VENDORS_AND_MANY_COMMERCE:
    :cvar EWHO_VOCABULARIES_IT_ADOPTION_M:
    """
    OSOFTWARE_WIDESPREAD_MUST_RE = "osoftware-widespread_must_re"
    VTO_SIGNIFICANT_GOVERNMENT_DISSEMINATE_INDUSTRY_A_OVER = "vto.significant_government_disseminate.industry.a_over"
    INDUSTRY_THE_IN_SPECIFICATIONS_THE_D = "_industry-the-in_specifications.the_d"
    HSYSTEMS_I = "hsystems-i"
    BRESOURCE_AND_C = "bresource.and-c"
    FBOTH_TH = "fboth-th"
    INVESTIGATION_OF_HELP_ITS_BE_SUPPORT_VENDORS_AND_MANY_COMMERCE = "_investigation.of-help_its-be_support.vendors_and_many-commerce"
    EWHO_VOCABULARIES_IT_ADOPTION_M = "ewho-vocabularies-it-adoption_m"


@dataclass
class NistschemaSvIvAtomicNcnameEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-NCName-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicNcnameEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
