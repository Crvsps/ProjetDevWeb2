<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12" >
                <h1 class="tiltle">Recherche</h1>
                <h2 class="is-size-5 has-text-grey">Terme de recherche: '{{query}}'</h2>
            </div>

            <ObjectBox
                v-for="object in objects"
                v-bind:key="object.id"
                v-bind:object="object"/>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ObjectBox from '@/components/ObjectBox.vue'

export default {
    name: "PageRecherche",
    components: {
        ObjectBox
    },
    data() {
        return {
            objects: [],
            query:""
        }
    },
    mounted () {
        document.title = 'Recherche | CYber School'
        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
         performSearch() {
            axios
            .post ('/api/v1/objets/search/', {"query":this.query})
            .then (response => {
                this.objects = response.data
            })
            .catch(error =>{
                console.log(error)
            })
        }
    }
}
</script>