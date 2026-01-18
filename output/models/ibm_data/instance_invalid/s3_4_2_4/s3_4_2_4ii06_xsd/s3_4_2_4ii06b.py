from __future__ import annotations

from dataclasses import dataclass

from output.models.ibm_data.instance_invalid.s3_4_2_4.s3_4_2_4ii06_xsd.s3_4_2_4ii06 import (
    C1,
)

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_2_4"


@dataclass(kw_only=True)
class Root(C1):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_2_4"
