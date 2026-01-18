from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-enumeration-3-NS"


class NistschemaSvIvAtomicNameEnumeration3Type(Enum):
    UPROCESSORS_FOR_PUBLISHING_METHODS_FOR_AN_WITH_INCLUDED_IMPLEME = (
        "uprocessors:for.publishing:methods.for:an-with:included:impleme"
    )
    AND_DAT = "_and-dat"
    IBUSINESS_PROCESSES_LANGUAGE_CHAIN = "ibusiness_processes-language-chain"
    SPECIFICATIO = ":specificatio"
    MEDIUM_SIZED_TESTING_TO_USERS_AND_REGISTRIES_SU = (
        ":medium-sized-testing-to:users:and-registries_su"
    )
    TO_THE_HAS_TO_LAUNCHI = "_to_the:has_to:launchi"
    GPROVIDE_BACK_THE_ARE_AND_SHIFT_AND_CREATION_IS = (
        "gprovide-back.the-are:and_shift.and-creation:is-"
    )


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNameEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-Name-enumeration-3-NS"

    value: NistschemaSvIvAtomicNameEnumeration3Type = field(
        metadata={
            "required": True,
        }
    )
