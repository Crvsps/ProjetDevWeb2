<template>
  <div class="reset-password-container">
    <h2>Réinitialiser votre mot de passe</h2>
    <form @submit.prevent="handleSubmit" class="reset-password-form">
      <!-- Champ pour l'email -->
      <div class="form-group">
        <label for="email">Email</label>
        <input
          v-model="email"
          type="email"
          id="email"
          placeholder="Entrez votre email"
        />
      </div>

      <!-- Bouton de soumission -->
      <button type="submit">Réinitialiser</button>
    </form>

    <!-- Message de succès après soumission -->
  </div>
</template>


<style>
/* Style général du formulaire de réinitialisation de mot de passe */
.reset-password-container {
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
  background-color: darkblue;
}

button:disabled {
  background-color: #ddd;
}

.error {
  color: red;
  font-size: 12px;
}

.success-message {
  background-color: #d4edda;
  color: blue;
  border: 1px solid #c3e6cb;
  padding: 10px;
  border-radius: 4px;
  margin-top: 20px;
}
</style>
