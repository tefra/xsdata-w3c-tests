from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-enumeration-5-NS"


class NistschemaSvIvAtomicNcnameEnumeration5Type(Enum):
    """
    :cvar KOBJECT_TRANSACT_CONSTITUENT_OF_FILE_IS_WITHOUT_ABOUT_ARE_A_BE:
    :cvar OCONTRIBU:
    :cvar DOF_SET_WIRELESS_BUILDIN:
    :cvar UAND_MANIPULATION_GOOD_INFORMATION_AMBIGUITIES:
    :cvar TTHROUGH_OF_AV:
    :cvar DIVISIONS_YEARS_FOR_PARTNERSHIP_FED:
    :cvar ANEUTRAL_HETEROGENEOUS_REPRODUCED_WILL:
    :cvar AND_TO_WE_FRAMEWORKS_PERVASIVE_THE_REGI:
    :cvar UIN_AND_ENSURE:
    """
    KOBJECT_TRANSACT_CONSTITUENT_OF_FILE_IS_WITHOUT_ABOUT_ARE_A_BE = "kobject-transact-constituent_of_file.is_without_about_are_a.be"
    OCONTRIBU = "ocontribu"
    DOF_SET_WIRELESS_BUILDIN = "dof_set.wireless-buildin"
    UAND_MANIPULATION_GOOD_INFORMATION_AMBIGUITIES = "uand-manipulation.good.information.ambiguities-"
    TTHROUGH_OF_AV = "tthrough-of_av"
    DIVISIONS_YEARS_FOR_PARTNERSHIP_FED = "_divisions.years_for_partnership-fed-"
    ANEUTRAL_HETEROGENEOUS_REPRODUCED_WILL = "aneutral_heterogeneous.reproduced-will_"
    AND_TO_WE_FRAMEWORKS_PERVASIVE_THE_REGI = "_and.to-we_frameworks-pervasive_the-regi"
    UIN_AND_ENSURE = "uin-and-ensure."


@dataclass
class NistschemaSvIvAtomicNcnameEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-NCName-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicNcnameEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
