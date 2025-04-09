<template>
  <div class="profile-container">
    <div class="profile-header">
      <img alt="Photo de profil" class="profile-photo"/>
      <h1>Nom Prénom</h1>
      <p> email </p>
    </div>
    
    <div class="profile-edit">
      <h2>Modifier le profil</h2>
      <form>
        <label for="name">Nom</label>
        <input type="text" id="name" placeholder="Nom"/>

        <label for="firstname">Prénom</label>
        <input type="text"  id="firstname" placeholder="Prénom"/>

        <label for="email">Email</label>
        <input type="email" id="email" placeholder="Votre email"/>

        <label for="photo">Photo de profil</label>
        <input type="file" @change="onFileChange" id="photo"/>

        <button type="submit">Mettre à jour</button>
      </form>
    </div>
  </div>
</template>

// Renommer Profil.vue en ProfilPage.vue
<script lang="ts">
export default {
  name: 'ProfilPage'
}
</script>

<style>
.profile-container {
  width: 60%;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
}

.profile-header {
  text-align: center;
  margin-bottom: 20px;
}

.profile-photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
}

.profile-edit form {
  display: flex;
  flex-direction: column;
}

.profile-edit form label {
  margin-top: 10px;
}

.profile-edit form input {
  padding: 10px;
  margin-top: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.profile-edit form button {
  padding: 10px;
  background-color:blue;
  color: white;
  border: none;
  border-radius: 5px;
  margin-top: 20px;
  cursor: pointer;
}

.profile-edit form button:hover {
  background-color: darkblue;
}
</style>
