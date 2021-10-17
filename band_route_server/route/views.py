import json

# python file imports
from . import HeldKarpAlgorithm, DataConversion, NearestNeighborSolution

# third party imports
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
import jsonschema


class OptimalRoute(APIView):

    # Set default renderer
    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):

        # Get input from user
        try:
            points = json.loads(request.query_params['points'])
        except Exception as e:
            return Response(data=str(e), status=400, exception=True)

        # Validate JSON, must be in this format [{"x": number, "y": number}, {"x": number, "y": number}]
        try:
            DataConversion.JSON_validation(points)
        except jsonschema.exceptions.ValidationError as e:
            return Response(data=str(e), status=400, exception=True)

        # Use inputted json data to find distance and path
        try:
            # Convert inputted data into a data matrix
            distances = DataConversion.create_DM(points)

            # Get distance and path using Held-Karp Algorithm.
            distance, path = HeldKarpAlgorithm.held_karp(distances)
        except Exception as e:
            return Response(data=str(e), status=500, exception=True)

        # Create JSON payload to return data.
        data = {
            'distance': distance,
            'path': path
        }

        # Return payload
        return Response(data)


class EfficientRoute(APIView):

    # Set default renderer
    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):

        # Get input from user
        try:
            points = json.loads(request.query_params['points'])
        except Exception as e:
            return Response(data=str(e), status=400, exception=True)

        # Validate JSON, must be in this format [{"x": number, "y": number}, {"x": number, "y": number}]
        try:
            DataConversion.JSON_validation(points)
        except jsonschema.exceptions.ValidationError as e:
            return Response(data=str(e), status=400, exception=True)

        # Use inputted json data to find distance and path
        try:
            # Convert inputted data into a data matrix
            distances = DataConversion.create_DM(points)

            # Get distance and path using nearest neighbor solution.
            distance, path = NearestNeighborSolution.nearest_neighbor(distances)
        except Exception as e:
            return Response(data=str(e), status=500, exception=True)

        # Create JSON payload to return data.
        data = {
            'distance': distance,
            'path': path
        }

        # Return payload
        return Response(data)
