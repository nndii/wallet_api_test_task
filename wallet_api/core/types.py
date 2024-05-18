from typing import TypeAlias, Union

JSONVal: TypeAlias = Union[None, bool, str, float, int, "JSONArray", "JSONObject"]
JSONArray: TypeAlias = list[JSONVal]
JSONObject: TypeAlias = dict[str, JSONVal]
