from cgitb import reset
from os import stat
from urllib import response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, force_authenticate
import pytest
from store.models import Collection
from model_bakery import baker


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        response = create_collection({'title':'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_user_is_not_admin_returns_403(self, create_collection, authenticate):
        #arrange
        authenticate(is_staff=False)
        #act
        response = create_collection({'title':'a'})
        #assert
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_if_data_is_invalid_returns_400(self, create_collection, authenticate):
        authenticate(is_staff=True)
        
        response = create_collection({'title':''})
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
        
    def test_if_data_is_valid_returns_201(self, create_collection, authenticate):
        authenticate(is_staff=True)
        response = create_collection({'title':'a'})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
        
        
@pytest.fixture
def list_collection(api_client):
    def do_list_collection():
        return api_client.get('/store/collections/')
    return do_list_collection


@pytest.mark.django_db
class TestListCollection:
    def test_if_user_is_anonymous_returns_200(self, list_collection):
        response = list_collection()
        
        assert response.status_code == status.HTTP_200_OK
    
    def test_if_user_is_not_admin_returns_200(self, list_collection, authenticate):
        authenticate(is_staff=False)

        response = list_collection()

        assert response.status_code == status.HTTP_200_OK
        
    def test_if_user_is_admin_return_200(self, list_collection, authenticate):
        authenticate(is_staff=True)
        
        response = list_collection()
        
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_colection_exists_return_200(self, api_client):
        collection = baker.make(Collection)
        
        response = api_client.get(f'/store/collections/{collection.id}/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id' : collection.id,
            'title' : collection.title,
            'products_count' : 0
        }
    

