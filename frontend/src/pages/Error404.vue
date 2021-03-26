<template>
  <div class="fullscreen bg-white text-black text-center q-pa-md flex flex-center">
    <div>
      <div style="font-size: 10vh">
        404
      </div>

      <div class="text-h2" style="opacity:.4">
        That page doesn't exist...
      </div>

      <q-btn
        class="q-mt-xl"
        color="primary"
        text-color="white"
        glossy
        unelevated
        to="/"
        label="Go Home"
        no-caps
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Error404'
}
</script>
