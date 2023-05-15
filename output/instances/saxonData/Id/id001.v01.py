from output.models.saxon_data.id.id001_xsd.id001 import Doc
from output.models.saxon_data.id.id001_xsd.id001 import Para


obj = Doc(
    para=[
        Para(
            id_one="aaa",
            id_two="bbb"
        ),
        Para(
            id_one="ccc",
            id_two="ddd"
        ),
        Para(
            id_one="eee",
            id_two="eee"
        ),
    ]
)
