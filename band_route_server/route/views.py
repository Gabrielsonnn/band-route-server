from django.shortcuts import render
from django.http import JsonResponse
import json
from . import HeldKarpAlgorithm, DataConversion, NearestNeighborSolution

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView


class OptimalRoute(APIView):
    def get(self, request, *args, **kwargs):
        # Get input from user
        points = request.query_params['points']

        # Convert inputted data into a data matrix, expecting
        distances = DataConversion.create_DM(points)

        # input data matrix into Held-Karp Algorithm
        distance, path = HeldKarpAlgorithm.held_karp(distances)

        # Return JSON
        return Response(data)

class EfficientRoute(APIView):
    def get(self, request, *args, **kwargs):
        # Get input from user

        points = json.loads(request.query_params['points'])

        # Convert inputted data into a data matrix, expecting
        distances = DataConversion.create_DM(points)

        # Get path using nearest neighbor solution.
        distance, path = NearestNeighborSolution.nearest_neighbor(distances)

        # Return JSON
        return Response(data)

