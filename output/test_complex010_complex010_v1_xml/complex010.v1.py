from decimal import Decimal
from output.models.saxon_data.complex.complex010_xsd.complex010 import Root


obj = Root(
    value=Decimal('1234'),
    no_namespace_schema_location='complex010.xsd'
)
