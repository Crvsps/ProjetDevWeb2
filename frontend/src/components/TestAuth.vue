<template>
    <div>
      <h2>Test Authentification</h2>
      <button @click="testAuth">Tester l'authentification</button>
      <div v-if="message">
        <p>{{ message }}</p>
        <p v-if="user">Connecté en tant que : {{ user }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import apiClient from '../api/axios';
  
  export default {
    name : "TestAuth",
    data() {
      return {
        message: '',
        user: ''
      };
    },
    methods: {
      testAuth() {
        apiClient.get('/api/v1/users/protected/')
          .then(response => {
            this.message = response.data.message;
            this.user = response.data.user;
          })
          .catch(error => {
            this.message = 'Non authentifié ou token invalide.';
            this.user = '';
          });
      }
    }
  };
  </script>
  