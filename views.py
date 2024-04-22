from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import React
from .serializer import UserInputSerializer
import pandas as pd
from sklearn.linear_model import LinearRegression

class UserInputViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserInputSerializer(data=request.data)
        if serializer.is_valid():
            # Extract validated data from serializer
            input1 = serializer.validated_data.get('input1')
            input2 = serializer.validated_data.get('input2')
            input3 = serializer.validated_data.get('input3')
            input4 = serializer.validated_data.get('input4')
            input5 = serializer.validated_data.get('input5')
            input6 = serializer.validated_data.get('input6')
            input7 = serializer.validated_data.get('input7')

            # Load the dataset
            df = pd.read_csv('C:\Users\Arul\Downloads\World Happiness Report.csv')

            # Drop the unnecessary column
            df = df.drop("Country or region", axis=1)

            # Split features and target
            X = df.drop("GDP per capita", axis=1)
            y = df["GDP per capita"]

            # Fit the regression model
            lr = LinearRegression()
            lr.fit(X, y)

            # Predict the output based on user input
            user_input = [[float(input1), float(input2), float(input3), float(input4), float(input5), float(input6), float(input7)]]
            prediction = lr.predict(user_input)

            # Return HTTP 200 OK with custom message
            return Response({'message': 'All OK'}, status=status.HTTP_200_OK)
        else:
            # Return serializer errors if data is invalid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
