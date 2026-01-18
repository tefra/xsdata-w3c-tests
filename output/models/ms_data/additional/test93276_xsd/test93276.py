from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.additional.test93276_xsd.test93276_types import (
    GlobalAddressTypeValues,
)

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class T0020V1Type:
    e: GlobalAddressTypeValues = field(
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root(T0020V1Type):
    class Meta:
        name = "root"
        namespace = "foo"
