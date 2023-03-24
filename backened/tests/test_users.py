import unittest
import json
from backened.routes.get_users import get_users
from backened.routes.register import user_register
from backened.routes.login import login
from backened.routes.get_user_uid import profile_view
from backened.main import create_app
from backened.sqlalchemy_db import db
from unittest import mock
from mock import patch
import pytest
import jwt
from werkzeug.datastructures import Headers

class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()

        self.appctx = self.app.app_context()
        self.request_ctx = self.app.test_request_context()

        self.request_ctx.push()

        self.client = self.app.test_client()      

        db.create_all()

    # def test_get_users(self):

        
    #     f = open('backened/tests/response.json')
    #     data = json.load(f)
    #     print("data", data)
    #     response = get_users()
    #     all_user = json.loads(response.data)
    #     print("111111111////////", all_user["Users"])
    #     assert data["body"] == all_user["Users"]
    #     assert response.status_code == 200



      
    
    
    @patch('backened.services.service_register.run_insert', return_value={'status': 'success'})
    def test_service_reg_return_correct_data(self, mock_insert):
        
        data = {                                                              
            "user_name": "testuser58",
            "password": "123456",
            "email_address": "testuser58@example.com",
            "dob": "2022-06-07 00:00:00",
            "address": "Ahmedabad",
            
        }
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.register.request", m1):
            
            response = user_register()
            
            mock_insert.assert_called_once() 
            self.assertEqual(response.json, {'Message': 'New user Created'},201) 
        
      
        
     
    def test_service_register_username_len_min5(self):
        
        data = {                                                              
            "user_name": "test",
            "password": "123456",
            "email_address": "testuser58@example.com",
            "dob": "2022-06-07 00:00:00",
            "address": "Ahmedabad",
            
        }
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.register.request", m1):
            
            response = user_register()
            self.assertEqual(response, ({'errors': {'user_name': ['Shorter than minimum length 5.']}}, 422)) 


    def test_service_register_username_required(self):  
        
        data = {                                                              
            
            "password": "123456",
            "email_address": "testuser58@example.com",
            "dob": "2022-06-07 00:00:00",
            "address": "Ahmedabad",
            
        }
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.register.request", m1):
            
            response = user_register()
            self.assertEqual(response, ({'errors': {'user_name': ['Missing data for required field.']}}, 422)) 
        
             
    def test_service_register_password_required(self):  
        
        data = {                                                              
            "user_name": "test5",
            
            "email_address": "testuser58@example.com",
            "dob": "2022-06-07 00:00:00",
            "address": "Ahmedabad",
            
        }
        
       
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.register.request", m1):
            
            response = user_register()
            self.assertEqual(response, ({'errors': {'password': ['Missing data for required field.']}}, 422))     


    
    def test_service_register_password_required_and_username_length_min5(self):  
        
        data = {                                                              
            "user_name": "test",
            "email_address": "testuser58@example.com",
            "dob": "2022-06-07 00:00:00",
            "address": "Ahmedabad",
            
        }
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.register.request", m1):
            
            response = user_register()
            self.assertEqual(response, ({'errors':  {
        "password": [
            "Missing data for required field."
        ],
        "user_name": [
            "Shorter than minimum length 5."
        ]
    }}, 422))


    def test_service_register_password_required_and_username_required(self):  
        
        data = {                                                              
           
            "email_address": "testuser58@example.com",
            "dob": "2022-06-07 00:00:00",
            "address": "Ahmedabad",
            
        }
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.register.request", m1):
            
            response = user_register()
            self.assertEqual(response, ({'errors':  {
        "password": [
            "Missing data for required field."
        ],
        "user_name": [
            "Missing data for required field."
        ]
    }}, 422))


     
    def test_service_reg_return_user_already_exist(self):
        
        data = {                                                              
            "user_name": "testuser58",
            "password": "123456",
            "email_address": "testuser58@example.com",
            "dob": "2022-06-07 00:00:00",
            "address": "Ahmedabad",
            
        }
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.register.request", m1):
            
            response = user_register()
            
            self.assertEqual(response.json, {'message': 'User already exist with this email address!'},201) 

    run_select_expected={
        'id': 201, 
        'user_name': 'testuser58', 
        'password': 'sha256$WbLrMDWEUHKvLDSC$2a051f8689222fc9815cd00da2c3260e114c313ba20edebf8df17e6d409721ac', 
        'email_address': 'testuser58@example.com', 
        'dob': '2022-06-07T23:16:20', 
        'uid': '75f9d2c5570f4c7bb5e28c5807f92c48'
    }

    @patch('backened.services.service_login.run_select_where', return_value = run_select_expected)
    def test_service_login_return_correct_data(self, mock_login):
        
        data = {                                                              
            "user_name": "testuser58",
            "password": "123456",
             }
        
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.login.request", m1):
            
            response = login()
            mock_login.assert_called_once()
            self.assertEqual(response.json, {
                'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXlsb2FkIjoie1xuICAgIFwiZG9iXCI6IFwiMjAyMi0wNi0wN1QyMzoxNjoyMFwiLFxuICAgIFwiZW1haWxfYWRkcmVzc1wiOiBcInRlc3R1c2VyNThAZXhhbXBsZS5jb21cIixcbiAgICBcImlkXCI6IDIwMSxcbiAgICBcInBhc3N3b3JkXCI6IFwic2hhMjU2JFdiTHJNRFdFVUhLdkxEU0MkMmEwNTFmODY4OTIyMmZjOTgxNWNkMDBkYTJjMzI2MGUxMTRjMzEzYmEyMGVkZWJmOGRmMTdlNmQ0MDk3MjFhY1wiLFxuICAgIFwidWlkXCI6IFwiNzVmOWQyYzU1NzBmNGM3YmI1ZTI4YzU4MDdmOTJjNDhcIixcbiAgICBcInVzZXJfbmFtZVwiOiBcInRlc3R1c2VyNThcIlxufSJ9.rWrD3jds4fOk64D2jqi6yfEbeXJUaNU8dYdDFkQ1Ehs'
            }) 
            self.assertEqual(response.status_code,201)

    
    @patch('backened.services.service_login.run_select_where')
    def test_service_login_return_no_user_found(self, mock_login):
        
        

        data = {                                                              
            "user_name": "testuser58",
            "password": "123456",
             }
          
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.login.request", m1):
            
            response = login()
            print("test_response", response.json)
            mock_login.assert_called_once()
            self.assertRaises(IndexError)
            self.assertEqual(response.status_code, 404)

    @patch('backened.services.service_login.run_select_where', return_value = run_select_expected)
    def test_service_login_user_mismatch(self, mock_login):
        
        data = {                                                              
            "user_name": "Testuser58",
            "password": "123456",
             }
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.login.request", m1):
            
            response = login()
            mock_login.assert_called_once()
            self.assertEqual(response.json, {'message': 'User Name mismatch. Please SignUp First!'}) 
            self.assertEqual(response.status_code,404)


    @patch('backened.services.service_login.run_select_where', return_value = run_select_expected)
    def test_service_login_wrong_password(self, mock_login):
        
        data = {                                                              
            "user_name": "testuser58",
            "password": "1234567",
             }
        
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.login.request", m1):
            
            response = login()
            mock_login.assert_called_once()
            self.assertEqual(response.json, {'message': 'Could not verify password!'}) 
            self.assertEqual(response.status_code,403)


    def test_service_login_username_len_min5(self):
        
        data = {                                                              
            "user_name": "test",
            "password": "123456",
           
        }
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.login.request", m1):
            
            response = login()
            self.assertEqual(response, ({'errors': {'user_name': ['Shorter than minimum length 5.']}}, 422)) 


    def test_service_login_username_required(self):  
        
        data = {                                                              
            "password": "123456",
            }
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.login.request", m1):
            
            response = login()
            self.assertEqual(response, ({'errors': {'user_name': ['Missing data for required field.']}}, 422)) 
        
             
    def test_service_login_password_required(self):  
        
        data = {                                                              
            "user_name": "test5",
            
        }
        
       
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.login.request", m1):
            
            response = login()
            self.assertEqual(response, ({'errors': {'password': ['Missing data for required field.']}}, 422))     


    
    def test_service_login_password_required_and_username_length_min5(self):  
        
        data = {                                                              
            "user_name": "test",
            
            
        }
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.login.request", m1):
            
            response = login()
            self.assertEqual(response, ({'errors':  {
        "password": [
            "Missing data for required field."
        ],
        "user_name": [
            "Shorter than minimum length 5."
        ]
    }}, 422))


    def test_service_login_password_required_and_username_required(self):  
        
        data = {}
        
        
        m1 = mock.MagicMock()
        m1.get_json.return_value = data
        print("m", m1)
        with mock.patch("backened.routes.login.request", m1):
            
            response = login()
            self.assertEqual(response, ({'errors':  {
        "password": [
            "Missing data for required field."
        ],
        "user_name": [
            "Missing data for required field."
        ]
    }}, 422))


    expected_profile_record ={
        
        "address": "Ahmedabad",
        "dob": "2022-06-07T23:16:20",
        "email_address": "testuser58@example.com",
        "id": 201,
        "password": "sha256$WbLrMDWEUHKvLDSC$2a051f8689222fc9815cd00da2c3260e114c313ba20edebf8df17e6d409721ac",
        "uid": "75f9d2c5570f4c7bb5e28c5807f92c48",
        "user_name": "testuser58"
}


    @patch(
        'backened.services.service_profile.run_select_where_uid', 
        return_value = expected_profile_record
    )
    def test_service_user_profile(self, mock_profile):

        data = {                                                              
            "user_name": "testuser58",
            "password": "123456",
            "email_address": "testuser58@example.com",
            "dob": "2022-06-07 00:00:00",
            "address": "Ahmedabad",
            
        }

        api_key_headers = Headers({
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXlsb2FkIjoie1xuICAgIFwiZG9iXCI6IFwiMjAyMi0wNi0wNyAwMDowMDowMFwiLFxuICAgIFwiZW1haWxfYWRkcmVzc1wiOiBcInRlc3R1c2VyNTdAZXhhbXBsZS5jb21cIixcbiAgICBcImlkXCI6IDIwMCxcbiAgICBcInBhc3N3b3JkXCI6IFwic2hhMjU2JGV2ckI4d2o5MmVpQTBGVTMkZWY1ZGYxYjU1ODI1ZTBkOWMwYmYyYTEyOTY5N2NhZmFmZDQzODllNWIwMzY5OGZhZjkxYTJkZDAyMjkwODU5ZFwiLFxuICAgIFwidWlkXCI6IFwiZTc0OWVlNjgzNzZmNGMzZGJlMmFjYzE1NmI4YjE3ZDhcIixcbiAgICBcInVzZXJfbmFtZVwiOiBcInRlc3R1c2VyNTdcIlxufSJ9.XI7QY5HqZfaJyzVgztU1Vr-d5GkOMyD_ZtC5-VJO8'
        })

        response = profile_view(data,"75f9d2c5570f4c7bb5e28c5807f92c48")
        mock_profile.assert_called_once()
        self.assertEqual(response.json, {} )
        self.assertEqual(response.status_code,403)