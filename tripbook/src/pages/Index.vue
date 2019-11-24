<template>
  <q-page class="row flex flex-center q-gutter-md q-pa-lg">
    <q-card class="col-12 row justify-center q-pa-md q-gutter-y-md column">
      <q-input
        v-model="search"
        outlined
        placeholder="Search"
      >
        <template v-slot:append>
          <q-icon name="search" />
        </template>
      </q-input>
    </q-card>
    <q-card
      class="my-card"
      v-for="i in 5"
      :key="i"
    >
      <img src="https://cdn.quasar.dev/img/parallax2.jpg">

      <q-list>
        <q-item clickable>
          <q-item-section avatar>
            <q-icon
              color="primary"
              name="local_bar"
            />
          </q-item-section>

          <q-item-section>
            <q-item-label>Bar XYZ</q-item-label>
            <q-item-label caption>Have a drink.</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable>
          <q-item-section avatar>
            <q-icon
              color="red"
              name="local_gas_station"
            />
          </q-item-section>

          <q-item-section>
            <q-item-label>Gas Station</q-item-label>
            <q-item-label caption>Fill your gas tank.</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable>
          <q-item-section avatar>
            <q-icon
              color="amber"
              name="local_movies"
            />
          </q-item-section>

          <q-item-section>
            <q-item-label>Cinema XYZ</q-item-label>
            <q-item-label caption>Watch a movie.</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-card>
  </q-page>
</template>

<script>
export default {
  name: 'PageIndex',
  data () {
    return {
      focusFilter: false,
      all_destination: []
    }
  },
  componentDidMount () {
    this.retrieve_suggestion()
  },
  methods: {
    retrieve_suggestion () {
      this.$axios.get('http://localhost:5000/get_my_suggestions').then(r => {
        this.all_destination = r.data
      }).catch(er => alert(er.toString()))
    }
  }
}
</script>

<style>
.my-card {
  max-width: 50vh;
}
</style>
