from decimal import Decimal
from output.models.sun_data.elem_decl.type_def.type_def00403m.type_def00403m_xsd.type_def00403m import Global
from output.models.sun_data.elem_decl.type_def.type_def00403m.type_def00403m_xsd.type_def00403m import GlobalPreDefinedType
from output.models.sun_data.elem_decl.type_def.type_def00403m.type_def00403m_xsd.type_def00403m import Root


obj = Root(
    global_value=Global(
        value=True
    ),
    global_pre_defined_type=GlobalPreDefinedType(
        value='true'
    ),
    local=Decimal('1.1'),
    local_pre_defined_type='1',
    local_inline='false'
)
