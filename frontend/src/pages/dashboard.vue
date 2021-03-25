<template>
  <q-page class="flex column container">

    <h1>Jobs</h1>

    <div v-for="(job,index) in filteredJobs" :key="index">
      <p>{{ job.role }}</p>
    </div>


  </q-page>
</template>

<script>

export default {
  data: () => ({
    jobs: [],
    filteredJobs: []
  }),
  mounted() {
    this.getJobs()
  },
  methods: {
    async getJobs() {
      const jobList = await this.$auth.axios({ url: 'jobs'})
      this.jobs = jobList.data

      this.filter('Senior')
    },
    filter(keyword) {
      this.filteredJobs = this.jobs.filter((job) => {
        return !job.role.includes(keyword)
      })
    }
  },
  computed: {
    authUserName() {
      const user = this.$auth.user()
      if (user) {
        return user.first_name
      };
    },
  },
};
</script>
