import requests 
import pytest
from classes.class_get import GET_REQUEST 
from jsons.jsons_for_get import class_jsons_for_get
from jsons.jsons_for_post import class_jsons_for_post_requests
from jsons.jsons_for_post import class_jsons_for_post_responses
from jsons.jsons_for_put_delete_patch import class_jsons_for_put_responses 
from jsons.jsons_for_put_delete_patch import class_jsons_for_put_requests 
from jsons.jsons_for_put_delete_patch import class_jsons_for_patch_responses 
from jsons.jsons_for_put_delete_patch import class_jsons_for_patch_requests 

class Test_API_GET:

    def test_LIST_USERS(self):
        GET_REQUEST.get_request_OK('https://reqres.in/api/users?page=2', class_jsons_for_get.body_LIST_USERS)

    def test_SINGLE_USER(self):
        GET_REQUEST.get_request_OK('https://reqres.in/api/users/2', class_jsons_for_get.body_SINGLE_USER)

    def test_SINGLE_USER_NOT_FOUND(self):
        GET_REQUEST.get_request_404('https://reqres.in/api/users/23', class_jsons_for_get.body_answer_for_404)

    def test_LIST_RESOURCE(self):
        GET_REQUEST.get_request_OK('https://reqres.in/api/unknown', class_jsons_for_get.body_LIST_RESOURCE)

    def test_SINGLE_RESOURCE(self):
        GET_REQUEST.get_request_OK('https://reqres.in/api/unknown/2', class_jsons_for_get.body_SINGLE_RESOURCE)

    def test_SINGLE_RESOURCE_NOT_FOUND(self):
        GET_REQUEST.get_request_404('https://reqres.in/api/unknown/23', class_jsons_for_get.body_answer_for_404)

    def test_DELAYED_RESPONSE(self):
        GET_REQUEST.get_request_OK('https://reqres.in/api/users?delay=3', class_jsons_for_get.body_DELAYED_RESPONSE)

class Test_API_POST:
    def test_CREATE(self):
        json_request= class_jsons_for_post_requests.body_CREATE
        post = requests.post('https://reqres.in/api/users', data=json_request, verify =False)
        assert post.status_code == 201, 'артефакт не создан'
        ans = post.json()
        ans['id'] = '0'
        ans['createdAt'] = '0'  
        assert str(ans) == class_jsons_for_post_responses.body_CREATE_ans, 'тело ответа некорректно'

    def test_LOGIN_UNSUCCESSFUL(self):
        json_request= class_jsons_for_post_requests.body_LOGIN_UNSUCCESSFUL
        post = requests.post('https://reqres.in/api/login', data=json_request, verify =False)
        assert post.status_code == 400, 'неверный код ошибки'
        assert str(post.json()) == class_jsons_for_post_responses.body_LOGIN_UNSUCCESSFUL_ans, 'тело ответа некорректно'

class Test_API_PUT:
    def test_UPDATE_PUT(self):
        json_request= class_jsons_for_put_requests.body_UPDATE_PUT
        put = requests.put('https://reqres.in/api/users/2', data=json_request, verify =False)
        assert put.status_code == 200, 'сообщение не доставлено'
        ans = put.json()
        ans['updatedAt'] = '0'  
        assert str(ans) == class_jsons_for_put_responses.body_UPDATE_PUT_ans, 'тело ответа некорректно'

class Test_API_DELETE:
    def test_DELETE(self):
        delete = requests.delete('https://reqres.in/api/users/2', verify =False)
        assert delete.status_code == 204, 'неверный код ошибки'

class Test_API_PATCH:
    def test_UPDATE_PATCH(self):
        json_request= class_jsons_for_patch_requests.body_UPDATE_PATCH
        patch = requests.patch('https://reqres.in/api/users/2', data=json_request, verify =False)
        assert patch.status_code == 200, 'сообщение не доставлено'
        ans = patch.json()
        ans['updatedAt'] = '0'  
        assert str(ans) == class_jsons_for_patch_responses.body_UPDATE_PATCH_ans, 'тело ответа некорректно'
