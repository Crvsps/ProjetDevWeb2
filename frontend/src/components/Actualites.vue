<template>
  <div class="actualites-container">
    <h1 class="title">Actualités CYber School</h1>

    <div class="filters">
      <select v-model="selectedCategory" class="filter-select">
        <option value="">Toutes les catégories</option>
        <option value="evenements">Évènements</option>
        <option value="nouveautes">Nouveautés</option>
        <option value="maintenance">Maintenance</option>
      </select>
    </div>

    <div class="articles-grid">
      <article v-for="article in filteredArticles" :key="article.id" class="article-card">
        <div class="article-image">
          <img :src="article.image" :alt="article.title">
        </div>
        <div class="article-content">
          <span class="article-date">{{ formatDate(article.date) }}</span>
          <h2>{{ article.title }}</h2>
          <p>{{ article.excerpt }}</p>
          <button class="read-more" @click="showArticle(article)">Lire la suite</button>
        </div>
      </article>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

interface Article {
  id: number;
  title: string;
  excerpt: string;
  content: string;
  date: string;
  category: string;
  image: string;
}

interface ComponentData {
  selectedCategory: string;
  articles: Article[];
}


export default defineComponent({
  name: 'ActualitesSchool',
  data() {
    return {
      selectedCategory: '',
      articles: [
        {
          id: 1,
          title: "Nouvelle Version de la Plateforme",
          excerpt: "Découvrez les nouvelles fonctionnalités de notre plateforme...",
          content: "Contenu complet de l'article...",
          date: "2024-03-15",
          category: "nouveautes",
          image: require("../assets/free.jpg")
        },
        {
          id: 2,
          title: "Maintenance Prévue",
          excerpt: "Une maintenance sera effectuée le weekend prochain...",
          content: "Contenu complet de l'article...",
          date: "2024-03-14",
          category: "maintenance",
          image: require("../assets/bird.jpg")
        },
        {
          id: 3,
          title: "Hackathon CYber School",
          excerpt: "Participez à notre prochain hackathon...",
          content: "Contenu complet de l'article...",
          date: "2024-03-13",
          category: "evenements",
          image: require("../assets/nerd.png")
        }
      ]
    }
  },
  computed: {
    filteredArticles(): Article[] {
      if (!this.selectedCategory) return this.articles
      return this.articles.filter((article: Article) => article.category === this.selectedCategory)
    }
  },
  
  methods: {
    formatDate(date: string): string {
      return new Date(date).toLocaleDateString('fr-FR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    },
    showArticle(article: Article): void {
      console.log('Show article:', article.id)
    }
  }
})
</script>

<style scoped>
.actualites-container {
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

.filters {
  margin-bottom: 2rem;
  text-align: right;
}

.filter-select {
  padding: 0.5rem;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}

.articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
}

.article-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.article-card:hover {
  transform: translateY(-5px);
}

.article-image {
  height: 200px;
  overflow: hidden;
}

.article-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.article-content {
  padding: 1.5rem;
}

.article-date {
  color: #6b7280;
  font-size: 0.875rem;
}

.article-content h2 {
  margin: 0.5rem 0;
  color: #1f2937;
  font-size: 1.25rem;
}

.read-more {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  margin-top: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.read-more:hover {
  background: #2563eb;
}

@media (max-width: 768px) {
  .articles-grid {
    grid-template-columns: 1fr;
  }
  
  .title {
    font-size: 2rem;
  }
}
</style>