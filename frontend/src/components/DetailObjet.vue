<template>
    <div class ="page-product">
        <div class = columsn is-multiple>
            <div class ='column is-9'>
                <figure class ="image mb-6">
                    <img v-bind:src="objet.get_image">
                </figure>
                <h1 class="Title">{{ objet.name }} </h1>
                <p> {{ objet.description }}</p>
                </div>
                <div class = "column is-3">
                    <h2 class ="subtitle">Informations</h2>
                    <p><strong>Statut: </strong>{{ objet.status }}</p>
                    <p><strong>Ajouté le: </strong>{{ formatDate(objet.date_added) }}</p>
                    <p><strong>Catégorie: </strong>{{ objet && objet.category ? objet.category.name : ''}}</p>
                    <div class = "field has-addons mt-6">
                    </div>
                </div>
            </div>
        </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'DetailObjet',
    data() {
        return {
            objet:{}
           }
    },
    mounted() {
        this.getObjet()
    },
    methods:{
        getObjet(){
            const category_slug = this.$route.params.category_slug
            const object_slug = this.$route.params.object_slug
            axios
                .get(`/api/v1/objets/${category_slug}/${object_slug}`)
                .then(response => {
                    console.log(response, response.data)
                    this.objet = response.data
                })
                .catch(error => {
                    console.log(error)
                })
                },
        formatDate(isoDate) {
            const date = new Date(isoDate)

            const formattedDate = date.toLocaleDateString('fr-FR', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            })

             const formattedTime = date.toLocaleTimeString('fr-FR', {
                hour: '2-digit',
                minute: '2-digit'
            })

            return `${formattedDate} à ${formattedTime}`
            },
        }           
}
</script>