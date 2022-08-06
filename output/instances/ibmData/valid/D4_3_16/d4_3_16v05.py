from output.models.ibm_data.valid.d4_3_16.d4_3_16v05_xsd.d4_3_16v05 import ElEnumerationAValue
from output.models.ibm_data.valid.d4_3_16.d4_3_16v05_xsd.d4_3_16v05 import ElEnumerationBValue
from output.models.ibm_data.valid.d4_3_16.d4_3_16v05_xsd.d4_3_16v05 import ElEnumerationCValue
from output.models.ibm_data.valid.d4_3_16.d4_3_16v05_xsd.d4_3_16v05 import Root


obj = Root(
    el_enumeration_a=[
        ElEnumerationAValue.VALUE_1999_01_01_T01_01_00_Z,
        ElEnumerationAValue.VALUE_2000_01_01_T01_01_00_01_00,
        ElEnumerationAValue.VALUE_2001_01_01_T01_01_00_01_00,
        ElEnumerationAValue.VALUE_2002_01_01_T01_01_00,
    ],
    el_enumeration_b=[
        ElEnumerationBValue.VALUE_2003_01_01_T01_01_00,
    ],
    el_enumeration_c=[
        ElEnumerationCValue.VALUE_1994_01_01_T01_01_00_Z,
        ElEnumerationCValue.VALUE_2005_01_01_T01_01_00_01_00,
        ElEnumerationCValue.VALUE_2006_01_01_T01_01_00_01_00,
    ]
)
