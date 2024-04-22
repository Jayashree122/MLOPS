from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import React

class UserInputTests(APITestCase):
    def test_create_user_input(self):
        # Define the URL for creating a new user input
        url = reverse('userinput-list')
        
        # Define the data to be sent in the POST request
        data = {
            'Overall_rank': 'value1',
            'Score': 'value2',
            'Social_support': 'value3',
            'Healthy_life_expectancy': 'value4',
            'Freedom_to_make_life_choices': 'value5',
            'Generosity': 'value6',
            'Perceptions_of_corruption': 'value7'
        }
        
        # Make a POST request to create a new user input
        response = self.client.post(url, data, format='json')
        
        # Assert that the request was successful (HTTP status code 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Assert that the new user input was created in the database
        self.assertEqual(React.objects.count(), 1)
        
        # Assert that the created user input has the correct values
        created_input = React.objects.get()
        self.assertEqual(created_input.Overall_rank, 'value1')
        self.assertEqual(created_input.Score, 'value2')
        self.assertEqual(created_input.Social_support, 'value3')
        self.assertEqual(created_input.Healthy_life_expectancy, 'value4')
        self.assertEqual(created_input.Freedom_to_make_life_choices, 'value5')
        self.assertEqual(created_input.Generosity, 'value6')
        self.assertEqual(created_input.Perceptions_of_corruption, 'value7')
