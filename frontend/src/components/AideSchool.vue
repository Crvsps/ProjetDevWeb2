<template>
  <div class="aide-container">
    <h1 class="title">Centre d'aide</h1>
    
    <div class="aide-section">
      <h2>FAQ</h2>
      <div class="faq-item" v-for="(item, index) in faqItems" :key="index">
        <details>
          <summary>{{ item.question }}</summary>
          <div class="faq-content">
            <p>{{ item.reponse }}</p>
          </div>
        </details>
      </div>
    </div>

    <div class="aide-section">
      <h2>Informations</h2>
      <div class="guides-grid">
        <div class="guide-card" v-for="(guide, index) in guides" :key="index">
          <h3>{{ guide.titre }}</h3>
          <p>{{ guide.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'AideSchool',
  data() {
    return {
      faqItems: [
        {
          question: "A quoi sert le site ?",
          reponse: "Ce site centralise toutes les informations de l'établissement, à commencer par les menus du jour, les différents objets connecté du bâtiment, des analyses pdf de l'utilisation et autres..."
        },
        {
          question: "Pourquoi créer un compte ?",
          reponse: "Pour devenir vous même acteur ! En vous créant un compte, vous pouvez accéder à plus d'informations concernant l'école qu'un visiteur classique, vous pouvez également vous faire valider par un admin afin d'obtenir un grade supérieur et ajouter des objets connecté, modérer les utilisateurs etc."
        },
        {
          question: "Comment créer un compte ?",
          reponse: "Cliquez sur 'Créer un compte' en haut à droite et remplissez le formulaire."
        },
        {
          question: "Comment ajouter un objet ?",
          reponse: "Une fois le compte crée, allez dans votre profil, cliquez sur 'Ajouter un objet' et remplissez les informations."
        }
      ],
      guides: [
        {
          titre: "Architecture du site",
          description: "Le site a été entièrement codé en Vue.Js et en django avec un système de base de données en sqlite"
        },
        {
          titre: "Contact",
          description: "Si vous avez des questions, veuillez vous adresser par mail à : contact@cyberschool.com"
        },
        {
          titre: "Créateurs",
          description: "Le site a été codé par Arthur, Lohan, Heeshaam, Yannis et Shawrov."
        }
      ]
    }
  }
})
</script>

<style scoped>
.aide-container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.title {
  font-size: 2.5rem;
  color: #2563eb;
  margin-bottom: 2rem;
  text-align: center;
}

.aide-section {
  margin-bottom: 3rem;
}

.aide-section h2 {
  font-size: 1.8rem;
  color: #1f2937;
  margin-bottom: 1.5rem;
}

.faq-item {
  margin-bottom: 1rem;
}

details {
  background: white;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

details:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);
}

details[open] {
  background: #f8fafc;
}

details[open] summary ~ * {
  animation: slide-fade 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

summary {
  font-weight: 600;
  cursor: pointer;
  color: #3b82f6;
  list-style: none;
  position: relative;
  padding: 0.75rem 2.5rem 0.75rem 1rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

summary::-webkit-details-marker {
  display: none;
}

summary::after {
  content: '';
  position: absolute;
  right: 1rem;
  top: 50%;
  width: 12px;
  height: 12px;
  border-right: 2px solid #3b82f6;
  border-bottom: 2px solid #3b82f6;
  transform-origin: center;
  transition: transform 0.3s ease;
  transform: translateY(-50%) rotate(45deg);
}

details[open] summary::after {
  transform: translateY(-50%) rotate(-135deg);
}

.faq-content {
  padding: 1rem;
  color: #4b5563;
  line-height: 1.6;
}

@keyframes slide-fade {
  0% {
    opacity: 0;
    transform: translateY(-8px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.guides-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.guide-card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.guide-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);
}

.guide-card h3 {
  color: #3b82f6;
  margin-bottom: 0.5rem;
}

@media (max-width: 768px) {
  .title {
    font-size: 2rem;
  }

  .aide-section h2 {
    font-size: 1.5rem;
  }

  .guides-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .aide-container {
    margin: 1rem auto;
  }

  details, .guide-card {
    padding: 0.75rem;
  }
}
</style>