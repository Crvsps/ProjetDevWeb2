<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img v-if="object && object.get_thumbnail" :src="object.get_thumbnail" alt="Produit">
            </figure>
            <h3 class="is-size-4">{{ object.name }}</h3>
            <p class=is-size-6 has-text-grey>{{ object.status }}</p>

            <router-link v-bind:to="object.get_absolute_url" class="button is-dark mt-4">Détails</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ObjectBox',
    props:{
        object: Object
    }
}
</script>

<style scoped>
.image{
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
}
</style>