<template>
  <div class="login-container">
    <h2>Connexion</h2>
    <form @submit.prevent="handleSubmit" class="login-form">
      <!-- Email Input -->
      <div class="form-group">
        <label for="email">Email</label>
        <input v-model="email" type="email" id="email" placeholder="Entrez votre email"/>
      </div>

      <!-- Password Input -->
      <div class="form-group">
        <label for="password">Mot de passe</label>
        <input type="password" id="password" placeholder="Entrez votre mot de passe"/>
      </div>

      <!-- Submit Button -->
      <button type="submit">Se connecter</button>
    </form>
  </div>
</template>

<style>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

h2 {
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

input {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

input.is-invalid {
  border-color: red;
}

button {
  width: 100%;
  padding: 10px;
  background-color: blue;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover{
  cursor: pointer;
  background-color: darkblue;
}

button:disabled {
  background-color: #ddd;
}

.error {
  color: red;
  font-size: 12px;
}
</style>
