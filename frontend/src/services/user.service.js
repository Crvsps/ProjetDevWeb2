import apiClient from '../api/axios';

class UserService {
  register(user) {
    return apiClient.post('/api/v1/users/register/', {
      username: user.username,
      password: user.password,
      password2: user.password2,
      email: user.email
    });
  }

  login(user) {
    return apiClient.post('/api/v1/users/login/', {
      username: user.username,
      password: user.password
    })
    .then(response => {
      if (response.data.token) {
        localStorage.setItem('token', response.data.token); 
      }
      console.log(localStorage.getItem('token')); 
      return response.data;
    });
  }
  
  

  logout() {
    return apiClient.post('/api/v1/users/logout/')
      .then(() => {
        localStorage.removeItem('token');
        window.location.href = '/login';  
      });
  }

  getCurrentUser() {
    return apiClient.get('/api/v1/users/me/');  
  }

  getUserProfile() {
    return apiClient.get('/api/v1/users/profile/');  
}
}

export default new UserService();