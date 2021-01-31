from django.urls import reverse
import pytest
from rest_framework import status



def test_hello_world():
	assert "hello_world" == "hello_world"
	assert "foo" != "bar"



def test_list(client):
	response = client.get("version1", format='json')
	print(response.status_code)
	assert response.status_code, status.HTTP_200_OK
	