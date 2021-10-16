import math
import json
import jsonschema
from jsonschema import validate


def create_DM(points):
    """
    Converts list of x,y pairs into a data matrix showing distance.

    :param points: list of x,y pairs
    :return: Data Matrix
    """

    # Get amount of points submitted.
    length = len(points)

    # Create data matrix filled with 0's with a length of number of x,y pairs
    distance_DM = [[0] * length for i in range(length)]

    # Create data matrix using distance formula for two points.
    for i in range(length):
        for j in range(i + 1, length):
            distance_DM[i][j] = distance_DM[j][i] = math.sqrt(
                ((points[j]['x'] - points[i]['x']) ** 2) + ((points[j]['y'] - points[i]['y']) ** 2))

    # Return data matrix
    return distance_DM


def JSON_validation(my_json):
    """
    :param json: inputted json to validate
    :return: boolean. True: Json is valid, False: json is invalid.
    """
    # Create schema for expected json
    points_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "x": {"type": "number"},
                "y": {"type": "number"},
            },
            "additionalProperties": False
        },
        "additionalProperties": False
    }

    # validate user inputted json to see if it matches schemas
    validate(instance=my_json, schema=points_schema)
