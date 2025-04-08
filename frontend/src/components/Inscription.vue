<template>
  <div class="signup-container">
    <h2>Inscription</h2>
    <form @submit.prevent="handleSubmit" class="signup-form">
      <!-- Champ pour le nom -->
      <div class="form-group">
        <label for="name">Nom</label>
        <input
          v-model="name"
          type="text"
          id="name"
          placeholder="Entrez votre nom"
        />
      </div>

      <!-- Champ pour le prénom-->
      <div class="form-group">
        <label for="firstname">Prénom</label>
        <input
          v-model="firstname"
          type="text"
          id="firstname"
          placeholder="Entrez votre prénom"
        />
      </div>

      <!-- Champ pour le pseudonyme-->
      <div class="form-group">
        <label for="username">Pseudonyme</label>
        <input
          v-model="username"
          type="text"
          id="username"
          placeholder="Entrez votre pseudonyme"
        />
      </div>

      <!-- Champ pour l'email -->
      <div class="form-group">
        <label for="email">Email</label>
        <input
          v-model="email"
          type="email"
          id="email"
          placeholder="Entrez votre Email"
        />
      </div>

      <!-- Champ pour le mot de passe -->
      <div class="form-group">
        <label for="password">Mot de passe</label>
        <input
          v-model="password"
          type="password"
          id="password"
          placeholder="Entrez votre mot de passe"
        />
      </div>

      <!-- Champ pour la confirmation du mot de passe -->
      <div class="form-group">
        <label for="confirmPassword">Confirmer le mot de passe</label>
        <input
          v-model="confirmPassword"
          type="password"
          id="confirmPassword"
          placeholder="Confirmez votre mot de passe"
        />
      </div>

      <!-- Bouton de soumission -->
      <button type="submit" :disabled="isSubmitting">S'inscrire</button>
    </form>
  </div>
</template>

<style>
/* Style général du formulaire d'inscription */
.signup-container {
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
