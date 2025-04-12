<template>
  <div class="connected-objects-container">
    <h2>Suivi des objets connectés</h2>

    <div v-for="objet in objets" :key="objet.id" class="device-card">
      <div class="device-info">
        <h3>{{ objet.nom || 'Nom non défini' }}</h3>
        <p><strong>Type :</strong> {{ objet.type || 'Type inconnu' }}</p>
        <p><strong>État :</strong> {{ objet.etat || 'État inconnu' }}</p>
        <p v-if="objet.consommation && objet.consommation.length">
          <strong>Consommation Moyenne :</strong>
          {{ calculMoyenne(objet).toFixed(2) }} kWh
        </p>
        <p v-else>
          <strong>Consommation Moyenne :</strong> Données non disponibles
        </p>
      </div>

      <div class="device-status">
        <p
          v-if="objet.consommation && objet.seuilCritique !== undefined && calculMoyenne(objet) > objet.seuilCritique"
          class="alert"
        >
          Consommation anormale détectée !
        </p>
        <p v-if="objet.maintenanceRequise" class="maintenance">
          Maintenance requise
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios' 

export default {
  name: 'SuiviObjets',
  data() {
    return {
      objets: [], // initialisé vide, les données	 viendront du backend
      loading: true,
      erreurChargement: null
    }
  },
  methods: {
    calculMoyenne(objet) {
      if (!objet || !objet.consommation || objet.consommation.length === 0) return 0;
      const total = objet.consommation.reduce((acc, val) => acc + (val.valeur || 0), 0);
      return total / objet.consommation.length;
    },

    // 🔽🔽🔽 DÉBUT : PARTIE À AJOUTER POUR APPELER LE BACKEND 🔽🔽🔽
    async fetchObjetsDepuisBackend() {
      try {
        const response = await axios.get('http://localhost:8000/api/objets/'); // ← ton endpoint Django
        this.objets = response.data.map(obj => ({ // définition des attributs de l'objet
          id: obj.id,
          nom: obj.nom,
          type: obj.type,
          etat: obj.etat,
          seuilCritique: obj.seuil_critique,
          maintenanceRequise: obj.maintenance_requise,
          consommation: obj.consommations
        }));
      } catch (error) { // gestion des erreurs
        this.erreurChargement = "Erreur lors du chargement des objets.";
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
    // 🔼🔼🔼 FIN : PARTIE BACKEND 🔼🔼🔼
  },

  mounted() {
    this.fetchObjetsDepuisBackend(); //backend appelé
  }
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
.device-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
  border-left: 5px solid #3b82f6;
}
.device-info h3 {
  margin: 0 0 0.5rem;
  color: #0f172a;
  font-size: 1.25rem;
}
.device-info p {
  margin: 0.25rem 0;
  color: #475569;
}
.device-status {
  min-width: 200px;
  text-align: right;
}
.alert {
  color: #ef4444;
  font-weight: 600;
}
.maintenance {
  color: #f59e0b;
  font-weight: 600;
}
</style>
