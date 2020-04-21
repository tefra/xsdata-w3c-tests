from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-enumeration-2-NS"


class NistschemaSvIvAtomicNcnameEnumeration2Type(Enum):
    """
    :cvar VALUE_INDUSTRY_THE_IN_SPECIFICATIONS_THE_D:
    :cvar VALUE_INVESTIGATION_OF_HELP_ITS_BE_SUPPORT_VENDORS_AND_MANY_COMMERCE:
    :cvar BRESOURCE_AND_C:
    :cvar EWHO_VOCABULARIES_IT_ADOPTION_M:
    :cvar FBOTH_TH:
    :cvar HSYSTEMS_I:
    :cvar OSOFTWARE_WIDESPREAD_MUST_RE:
    :cvar VTO_SIGNIFICANT_GOVERNMENT_DISSEMINATE_INDUSTRY_A_OVER:
    """
    VALUE_INDUSTRY_THE_IN_SPECIFICATIONS_THE_D = "_industry-the-in_specifications.the_d"
    VALUE_INVESTIGATION_OF_HELP_ITS_BE_SUPPORT_VENDORS_AND_MANY_COMMERCE = "_investigation.of-help_its-be_support.vendors_and_many-commerce"
    BRESOURCE_AND_C = "bresource.and-c"
    EWHO_VOCABULARIES_IT_ADOPTION_M = "ewho-vocabularies-it-adoption_m"
    FBOTH_TH = "fboth-th"
    HSYSTEMS_I = "hsystems-i"
    OSOFTWARE_WIDESPREAD_MUST_RE = "osoftware-widespread_must_re"
    VTO_SIGNIFICANT_GOVERNMENT_DISSEMINATE_INDUSTRY_A_OVER = "vto.significant_government_disseminate.industry.a_over"


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
        metadata=dict(
            required=True
        )
    )
