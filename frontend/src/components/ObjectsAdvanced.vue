<template>
  <div class="connected-objects-container">
    <h2>Objets connectés</h2>

    <!-- Formulaire -->
    <form @submit.prevent="handleSubmit" class="device-form">
      <div class="form-row">
        <input v-model="form.name" type="text" placeholder="Nom" required />
        <input v-model="form.description" type="text" placeholder="Description" required />
      </div>
      <div class="form-row">
        <select v-model="form.status" required>
          <option value="">Statut</option>
          <option value="active">Actif</option>
          <option value="inactive">Inactif</option>
        </select>
      </div>
      <button type="submit" class="btn-submit">{{ isEditing ? 'Modifier' : 'Ajouter' }}</button>
    </form>

    <!-- Liste des objets -->
    <table class="device-table">
      <thead>
        <tr>
          <th>Nom</th>
          <th>Description</th>
          <th>Statut</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="device in devices" :key="device.id">
          <td>{{ device.name }}</td>
          <td>{{ device.description }}</td>
          <td>{{ device.status }}</td>
          <td>
            <button class="btn-edit" @click="editDevice(device)">Modifier</button>
            <button class="btn-delete" @click="requestDeletion(device)">Demander suppression</button>
            <button class="btn-toggle" @click="toggleStatus(device)">Activer/Désactiver</button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-if="devices.length === 0" class="no-devices">Aucun objet connecté.</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface Device {
  id: number
  name: string
  description: string
  status: 'active' | 'inactive'
}
// Partie backend à insérer
const devices = ref<Device[]>([
  {
    id: 1,
    name: 'Caméra Extérieure',
    description: 'Caméra de surveillance du jardin',
    status: 'active',
  },
  {
    id: 2,
    name: 'Thermostat Salon',
    description: 'Thermostat intelligent',
    status: 'inactive',
  },
])
// Jusqu'ici

const form = ref<Partial<Device>>({
  name: '',
  description: '',
  status: '',
})

const isEditing = ref(false)
const editingId = ref<number | null>(null)

const handleSubmit = () => {
  if (isEditing.value && editingId.value !== null) {
    const index = devices.value.findIndex(d => d.id === editingId.value)
    if (index !== -1) {
      devices.value[index] = { ...(form.value as Device), id: editingId.value }
    }
    isEditing.value = false
    editingId.value = null
  } else {
    const newDevice: Device = {
      id: Date.now(),
      name: form.value.name!,
      description: form.value.description!,
      status: form.value.status as 'active' | 'inactive',
    }
    devices.value.push(newDevice)
  }

  resetForm()
}

const editDevice = (device: Device) => {
  form.value = { ...device }
  editingId.value = device.id
  isEditing.value = true
}

const requestDeletion = (device: Device) => {
  alert(`Demande envoyée à l’administrateur pour supprimer : ${device.name}`)
}

const toggleStatus = (device: Device) => {
  device.status = device.status === 'active' ? 'inactive' : 'active'
}

const resetForm = () => {
  form.value = {
    name: '',
    description: '',
    status: '',
  }
  isEditing.value = false
  editingId.value = null
}
</script>

<style scoped>
.connected-objects-container {
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
.device-form {
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

/* Tableau */
.device-table {
  width: 100%;
  border-collapse: collapse;
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.device-table th,
.device-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
  color: #475569;
}

.device-table th {
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

.btn-toggle {
  padding: 0.5rem 0.75rem;
  background-color: #10b981;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.btn-toggle:hover {
  background-color: #059669;
}

.no-devices {
  text-align: center;
  margin-top: 1.5rem;
  color: #94a3b8;
}
</style>
