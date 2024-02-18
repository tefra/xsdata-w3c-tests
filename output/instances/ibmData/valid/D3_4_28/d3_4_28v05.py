from output.models.ibm_data.valid.d3_4_28.d3_4_28v05_xsd.d3_4_28v05 import ElEnumerationA
from output.models.ibm_data.valid.d3_4_28.d3_4_28v05_xsd.d3_4_28v05 import ElEnumerationAValue
from output.models.ibm_data.valid.d3_4_28.d3_4_28v05_xsd.d3_4_28v05 import ElEnumerationB
from output.models.ibm_data.valid.d3_4_28.d3_4_28v05_xsd.d3_4_28v05 import ElEnumerationBValue
from output.models.ibm_data.valid.d3_4_28.d3_4_28v05_xsd.d3_4_28v05 import Root


obj = Root(
    el_enumeration_a=[
        ElEnumerationA(
            value=ElEnumerationAValue.VALUE_2002_02_02_T02_00_00_09_00
        ),
    ],
    el_enumeration_b=[
        ElEnumerationB(
            value=ElEnumerationBValue.VALUE_2006_02_02_T01_00_00_123_09_00
        ),
    ]
)
