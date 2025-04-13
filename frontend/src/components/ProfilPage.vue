<template>
  <div class="profile-container">
    <div class="profile-header">
      <img :src="user.photo || '/avatar-placeholder.png'" alt="Photo de profil" class="profile-photo" />
      <h1>{{ user.login }}</h1>
      <p>{{ user.email }}</p>
    </div>

    <div class="profile-edit">
      <h2>Modifier le profil</h2>
      <div v-if="successMessage" class="success-message">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>
      <form @submit.prevent="updateProfile" class="account-form">

        <!-- Section Publique -->
        <div class="section-title">Informations Publiques</div>

        <div class="form-group">
          <label for="login">Pseudonyme</label>
          <input type="text" v-model="updatedUser.login" id="login" placeholder="Pseudonyme" />
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" v-model="updatedUser.email" id="email" placeholder="Email" />
        </div>

        <div class="form-group">
          <label for="age">Âge</label>
          <input type="number" v-model="updatedUser.age" id="age" placeholder="Âge" />
        </div>

        <div class="form-group">
          <label for="genre">Genre</label>
          <input type="text" v-model="updatedUser.genre" id="genre" placeholder="Sexe / Genre" />
        </div>

        <div class="form-group">
          <label for="dateNaissance">Date de naissance</label>
          <input type="date" v-model="updatedUser.dateNaissance" id="dateNaissance" />
        </div>

        <div class="form-group">
          <label for="typeMembre">Type de membre</label>
          <input type="text" v-model="updatedUser.typeMembre" id="typeMembre" placeholder="Type de membre" readonly />
        </div>

        <!-- Section Privée -->
        <div class="section-title">Informations Privées</div>

        <div class="form-group">
          <label for="name">Nom</label>
          <input type="text" v-model="updatedUser.name" id="name" placeholder="Nom" />
        </div>

        <div class="form-group">
          <label for="fName">Prénom</label>
          <input type="text" v-model="updatedUser.fName" id="fName" placeholder="Prénom" />
        </div>

        <div class="form-group">
          <label for="password">Mot de passe</label>
          <input type="password" v-model="updatedUser.password" id="password" placeholder="Nouveau mot de passe" />
          <small class="password-hint">Laisser vide pour conserver le mot de passe actuel</small>
        </div>

        <!-- Photo -->
        <div class="form-group">
          <label for="photo">Photo de profil</label>
          <input type="file" @change="onFileChange" id="photo" accept="image/*" />
          <div class="preview-container" v-if="imagePreview">
            <img :src="imagePreview" alt="Aperçu de la photo" class="image-preview" />
          </div>
        </div>

        <div class="button-group">
          <button type="submit" class="btn-submit" :disabled="isSubmitting">
            {{ isSubmitting ? 'Mise à jour en cours...' : 'Mettre à jour' }}
          </button>
          <button type="button" class="btn-cancel" @click="resetForm">Annuler</button>
        </div>
      </form>
    </div>

    <!-- Accès au module Information si utilisateur simple -->
    <div v-if="user.typeMembre === 'simple'" class="information-module">
      <h3>Module Information</h3>
      <p>Ici s'affichera le contenu du module "Information" pour les utilisateurs simples.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        id: null,
        login: '',
        name: '',
        fName: '',
        email: '',
        age: '',
        genre: '',
        dateNaissance: '',
        typeMembre: '',
        photo: ''
      },
      updatedUser: {
        login: '',
        name: '',
        fName: '',
        email: '',
        age: '',
        genre: '',
        dateNaissance: '',
        typeMembre: '',
        photo: '',
        password: ''
      },
      imagePreview: null,
      isSubmitting: false,
      successMessage: '',
      errorMessage: ''
    };
  },
  created() {
    this.fetchUserProfile();
  },
  methods: {
    fetchUserProfile() {
      // Dans un cas réel, vous feriez un appel API pour récupérer les données du profil
      // Par exemple: axios.get('/api/profile')
      
      // Simulation de récupération des données
      setTimeout(() => {
        // Ces données viendraient normalement de votre API
        const userData = {
          id: 1,
          login: 'utilisateur123',
          name: 'Dupont',
          fName: 'Jean',
          email: 'jean.dupont@example.com',
          age: 32,
          genre: 'Homme',
          dateNaissance: '1991-05-15',
          typeMembre: 'simple',
          photo: 'https://via.placeholder.com/150'
        };
        
        // Mise à jour des données de l'utilisateur
        this.user = { ...userData };
        
        // Initialiser le formulaire avec les données actuelles
        this.resetForm();
      }, 500);
    },
    updateProfile() {
      this.isSubmitting = true;
      this.successMessage = '';
      this.errorMessage = '';
      
      // Dans un cas réel, vous enverriez les données à votre API
      // Par exemple: axios.put('/api/profile', this.updatedUser)
      
      // Simulation d'une mise à jour avec délai
      setTimeout(() => {
        try {
          // Ici, vous mettriez votre logique de validation
          if (!this.updatedUser.login) {
            throw new Error('Le pseudonyme est requis');
          }
          
          if (!this.updatedUser.email) {
            throw new Error('L\'email est requis');
          }
          
          // Mise à jour des données utilisateur (simulation)
          this.user = { ...this.updatedUser };
          
          // Si le mot de passe est vide, on ne le modifie pas
          if (!this.updatedUser.password) {
            delete this.user.password;
          }
          
          // Message de succès
          this.successMessage = 'Profil mis à jour avec succès !';
          
          // Dans un cas réel, vous pourriez rafraîchir le token ou les données de session
        } catch (error) {
          // Gestion des erreurs
          this.errorMessage = error.message || 'Une erreur est survenue lors de la mise à jour du profil';
        } finally {
          this.isSubmitting = false;
        }
      }, 1000);
    },
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        // Vérification du type de fichier
        if (!file.type.match('image.*')) {
          this.errorMessage = 'Veuillez sélectionner une image';
          return;
        }
        
        // Limiter la taille du fichier (par exemple à 2MB)
        if (file.size > 2 * 1024 * 1024) {
          this.errorMessage = 'L\'image ne doit pas dépasser 2MB';
          return;
        }
        
        const reader = new FileReader();
        reader.onload = (e) => {
          this.imagePreview = e.target.result;
          this.updatedUser.photo = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
    resetForm() {
      // Réinitialiser le formulaire avec les données actuelles de l'utilisateur
      this.updatedUser = { 
        ...this.user,
        password: '' // On ne remplit jamais le champ mot de passe
      };
      this.imagePreview = this.user.photo;
      this.successMessage = '';
      this.errorMessage = '';
    }
  }
};
</script>

<style scoped>
.profile-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  background: #f8fafc;
  min-height: 100vh;
}

.profile-header {
  text-align: center;
  margin-bottom: 2rem;
}

.profile-photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #e2e8f0;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.profile-edit {
  max-width: 600px;
  width: 100%;
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
  margin-bottom: 2rem;
}

.section-title {
  margin-top: 2rem;
  margin-bottom: 1rem;
  font-weight: 600;
  font-size: 1.2rem;
  color: #334155;
  border-bottom: 1px solid #e2e8f0;
  padding-bottom: 0.5rem;
}

.form-group {
  margin-bottom: 1.25rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #475569;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  background: #f9fafb;
}

input:focus {
  outline: none;
  border-color: #3b82f6;
  background: white;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
}

input[readonly] {
  background-color: #f1f5f9;
  cursor: not-allowed;
}

.password-hint {
  display: block;
  margin-top: 0.25rem;
  font-size: 0.85rem;
  color: #64748b;
}

.button-group {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}

.btn-submit {
  flex: 1;
  padding: 0.75rem;
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  color: white;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-submit:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.btn-submit:disabled {
  background: #94a3b8;
  cursor: not-allowed;
}

.btn-cancel {
  padding: 0.75rem 1.5rem;
  background: #f1f5f9;
  color: #334155;
  font-weight: 600;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-cancel:hover {
  background: #e2e8f0;
}

.success-message {
  background-color: #dcfce7;
  color: #166534;
  padding: 0.75rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  font-weight: 500;
}

.error-message {
  background-color: #fee2e2;
  color: #b91c1c;
  padding: 0.75rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  font-weight: 500;
}

.preview-container {
  margin-top: 1rem;
}

.image-preview {
  max-width: 150px;
  max-height: 150px;
  border-radius: 8px;
  border: 2px solid #e2e8f0;
}

.information-module {
  background: #e0f2fe;
  padding: 1.5rem;
  border-radius: 10px;
  width: 100%;
  max-width: 600px;
  text-align: center;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
}
</style>