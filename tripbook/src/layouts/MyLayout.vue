<template>
  <q-layout view="hHh lpR fFf">
    <q-header
      elevated
      class="bg-primary text-white"
    >
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="../assets/sad.svg" />
          </q-avatar>
          TripBook
        </q-toolbar-title>
        <!-- <q-btn flat round dense icon="group_add" class="q-mr-xs" /> -->
        <q-btn
          to="/trips"
          label="Start new Trip"
          color="positive"
          unelevated
        />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  data () {
    return {}
  }
}
</script>
