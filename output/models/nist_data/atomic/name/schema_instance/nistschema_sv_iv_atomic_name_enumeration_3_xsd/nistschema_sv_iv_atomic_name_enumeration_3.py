from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-enumeration-3-NS"


class NistschemaSvIvAtomicNameEnumeration3Type(Enum):
    """
    :cvar UPROCESSORS_FOR_PUBLISHING_METHODS_FOR_AN_WITH_INCLUDED_IMPLEME:
    :cvar AND_DAT:
    :cvar IBUSINESS_PROCESSES_LANGUAGE_CHAIN:
    :cvar SPECIFICATIO:
    :cvar MEDIUM_SIZED_TESTING_TO_USERS_AND_REGISTRIES_SU:
    :cvar TO_THE_HAS_TO_LAUNCHI:
    :cvar GPROVIDE_BACK_THE_ARE_AND_SHIFT_AND_CREATION_IS:
    """
    UPROCESSORS_FOR_PUBLISHING_METHODS_FOR_AN_WITH_INCLUDED_IMPLEME = "uprocessors:for.publishing:methods.for:an-with:included:impleme"
    AND_DAT = "_and-dat"
    IBUSINESS_PROCESSES_LANGUAGE_CHAIN = "ibusiness_processes-language-chain"
    SPECIFICATIO = ":specificatio"
    MEDIUM_SIZED_TESTING_TO_USERS_AND_REGISTRIES_SU = ":medium-sized-testing-to:users:and-registries_su"
    TO_THE_HAS_TO_LAUNCHI = "_to_the:has_to:launchi"
    GPROVIDE_BACK_THE_ARE_AND_SHIFT_AND_CREATION_IS = "gprovide-back.the-are:and_shift.and-creation:is-"


@dataclass
class NistschemaSvIvAtomicNameEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-Name-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicNameEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
