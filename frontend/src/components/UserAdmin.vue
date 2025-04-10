<template>
  <div class="user-manager-container">
    <h2>Liste des utilisateurs</h2>

    <!-- Formulaire d'ajout ou de modification -->
    <form @submit.prevent="handleSubmit" class="user-form">
      <div class="form-row">
        <input v-model="form.name" type="text" placeholder="Nom" required />
        <input v-model="form.email" type="email" placeholder="Email" required />
      </div>

      <div class="form-row">
        <select v-model="form.level" required>
          <option value="">Niveau</option>
          <option value="Débutant">Débutant</option>
          <option value="Intermédiaire">Intermédiaire</option>
          <option value="Avancé">Avancé</option>
					<option value="Expert">Expert</option>
        </select>
        <input v-model.number="form.points" type="number" placeholder="Points" required min="0" requierd max="7" />
      </div>

      <button type="submit" class="btn-submit">
        {{ isEditing ? 'Modifier' : 'Ajouter' }}
      </button>
    </form>

    <!-- Tableau des utilisateurs -->
    <table class="user-table">
      <thead>
        <tr>
          <th>Nom</th>
          <th>Email</th>
          <th>Niveau</th>
          <th>Points</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.name }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.level }}</td>
          <td>{{ user.points }}</td>
          <td>
            <button class="btn-edit" @click="editUser(user)">Modifier</button>
            <button class="btn-delete" @click="deleteUser(user.id)">Supprimer</button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-if="users.length === 0" class="no-users">Aucun utilisateur pour le moment.</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface User {
  id: number
  name: string
  email: string
  level: string
  points: number
}


// Insérer la partie backend de cette ligne 
const users = ref<User[]>([
  { id: 1, name: 'Alice Dupuis', email: 'alice@example.com', level: 'Débutant', points: 120 },
  { id: 2, name: 'Marc Legrand', email: 'marc@example.com', level: 'Intermédiaire', points: 340 },
  { id: 3, name: 'Sophie Lambert', email: 'sophie@example.com', level: 'Avancé', points: 560 },
])
// Jusqu'à cette ligne 

const form = ref<Partial<User>>({
  name: '',
  email: '',
  level: '',
  points: 0
})

const isEditing = ref(false)
const editingId = ref<number | null>(null)

const handleSubmit = () => {
  if (isEditing.value && editingId.value !== null) {
    // Modifier
    const index = users.value.findIndex(user => user.id === editingId.value)
    if (index !== -1) {
      users.value[index] = { ...(form.value as User), id: editingId.value }
    }
    isEditing.value = false
    editingId.value = null
  } else {
    // Ajouter
    const newUser: User = {
      id: Date.now(),
      name: form.value.name!,
      email: form.value.email!,
      level: form.value.level!,
      points: form.value.points!
    }
    users.value.push(newUser)
  }

  resetForm()
}

const editUser = (user: User) => {
  form.value = { ...user }
  editingId.value = user.id
  isEditing.value = true
}

const deleteUser = (id: number) => {
  users.value = users.value.filter(user => user.id !== id)
  if (editingId.value === id) {
    resetForm()
  }
}

const resetForm = () => {
  form.value = {
    name: '',
    email: '',
    level: '',
    points: 0
  }
  isEditing.value = false
  editingId.value = null
}
</script>

<style scoped>
.user-manager-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
  background: #f8fafc;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

h2 {
  color: #1e293b;
  text-align: center;
  margin-bottom: 2rem;
  font-size: 1.875rem;
  font-weight: 600;
}

/* Formulaire */
.user-form {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  margin-bottom: 2rem;
}

.form-row {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

input,
select {
  flex: 1;
  padding: 0.75rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  background: #f8fafc;
  transition: 0.3s ease;
}

input:focus,
select:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
  background: white;
}

.btn-submit {
  width: 100%;
  padding: 0.875rem;
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.user-table {
  width: 100%;
  border-collapse: collapse;
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.user-table th,
.user-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
  color: #475569;
}

.user-table th {
  background-color: #f1f5f9;
  font-weight: 600;
}

.btn-edit {
  margin-right: 0.5rem;
  padding: 0.5rem 0.75rem;
  background-color: #facc15;
  color: #1e293b;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.btn-edit:hover {
  background-color: #eab308;
}

.btn-delete {
  padding: 0.5rem 0.75rem;
  background-color: #ef4444;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.btn-delete:hover {
  background-color: #dc2626;
}

.no-users {
  text-align: center;
  margin-top: 1.5rem;
  color: #94a3b8;
}
</style>
