from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-enumeration-3-NS"


class NistschemaSvIvAtomicNameEnumeration3Type(Enum):
    """
    :cvar AND_DAT:
    :cvar GPROVIDE_BACK_THE_ARE_AND_SHIFT_AND_CREATION_IS:
    :cvar IBUSINESS_PROCESSES_LANGUAGE_CHAIN:
    :cvar MEDIUM_SIZED_TESTING_TO_USERS_AND_REGISTRIES_SU:
    :cvar SPECIFICATIO:
    :cvar TO_THE_HAS_TO_LAUNCHI:
    :cvar UPROCESSORS_FOR_PUBLISHING_METHODS_FOR_AN_WITH_INCLUDED_IMPLEME:
    """
    AND_DAT = "_and-dat"
    GPROVIDE_BACK_THE_ARE_AND_SHIFT_AND_CREATION_IS = "gprovide-back.the-are:and_shift.and-creation:is-"
    IBUSINESS_PROCESSES_LANGUAGE_CHAIN = "ibusiness_processes-language-chain"
    MEDIUM_SIZED_TESTING_TO_USERS_AND_REGISTRIES_SU = ":medium-sized-testing-to:users:and-registries_su"
    SPECIFICATIO = ":specificatio"
    TO_THE_HAS_TO_LAUNCHI = "_to_the:has_to:launchi"
    UPROCESSORS_FOR_PUBLISHING_METHODS_FOR_AN_WITH_INCLUDED_IMPLEME = "uprocessors:for.publishing:methods.for:an-with:included:impleme"


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
        metadata=dict(
            required=True
        )
    )
