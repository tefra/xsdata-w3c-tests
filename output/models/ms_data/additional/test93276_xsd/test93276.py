from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.additional.test93276_xsd.test93276_types import (
    GlobalAddressTypeValues,
)

__NAMESPACE__ = "foo"


@dataclass
class T0020V1Type:
    e: Optional[GlobalAddressTypeValues] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        },
    )


@dataclass
class Root(T0020V1Type):
    class Meta:
        name = "root"
        namespace = "foo"
