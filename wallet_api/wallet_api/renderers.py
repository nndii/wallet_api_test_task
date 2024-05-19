from decimal import Decimal
from typing import Any

from ninja.renderers import JSONRenderer
from ninja.responses import NinjaJSONEncoder
from pydantic.json import pydantic_encoder


class PydanticJSONEncoder(NinjaJSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, Decimal):
            return str(o)
        return pydantic_encoder(o)


class PydanticJSONRenderer(JSONRenderer):
    encoder_class = PydanticJSONEncoder
