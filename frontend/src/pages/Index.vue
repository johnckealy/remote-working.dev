<template>
  <q-page class="flex column container">
    <h1 class="text-h4 q-ma-lg">Remote Jobs</h1>

    <div class="row">
      <q-form
        class="col-md-6 col-12 q-pa-sm"
        @submit.prevent="submitIncludeChip"
      >
        <span class="text-subtitle1">Only include roles that mention...</span>
        <q-input
          outlined
          bottom-slots
          v-model="includeChip"
          placeholder="Junior, Java, etc.."
        >
          <q-btn
            class="q-px-sm p-ma-none"
            type="submit"
            round
            dense
            flat
            icon="add"
          />
        </q-input>
      </q-form>

      <q-form
        class="col-md-6 col-12 q-pa-sm"
        @submit.prevent="submitIgnoreChip"
      >
        <span class="text-subtitle1">Ignore roles that mention...</span>
        <q-input
          outlined
          bottom-slots
          v-model="ignoreChip"
          placeholder="Senior, .NET, etc.."
        >
          <q-btn
            class="q-px-sm p-ma-none"
            type="submit"
            round
            dense
            flat
            icon="add"
          />
        </q-input>
      </q-form>
    </div>

    <div>
      <q-chip
        v-for="(chip, includeIndex) in includeChips"
        :key="'a' + includeIndex"
        class="q-pa-md"
        @remove="removeIncludeChip(includeIndex)"
        color="primary"
        text-color="white"
        removable
      >
        {{ chip }}
      </q-chip>
      <q-chip
        v-for="(chip, ignoreIndex) in ignoreChips"
        :key="'b' + ignoreIndex"
        class="q-pa-md"
        @remove="removeIgnoreChip(ignoreIndex)"
        color="negative"
        text-color="white"
        removable
      >
        {{ chip }}
      </q-chip>
    </div>


    <div class="row">
      <q-space />
      <q-btn
        glossy
        class="q-mr-lg"
        color="primary"
        @click="saveFilters"
        >Save Filters</q-btn
      >
    </div>

    <strong v-if="resultsPerPageDisplay" class="q-ma-lg">Showing {{ resultsPerPageDisplay }} of {{ totalFilteredJobs }} jobs</strong>

    <q-spinner-dots class="q-mx-auto" size="100px" v-if="loading" color="primary" />

    <q-card v-else class="q-pa-md q-ma-xs" v-for="(job, i) of filteredJobs" :key="i">
      <div class="row items-center justify-between">
        <div class="col-12 col-md-4">
        <div class="">
          <span class="row text-h6 job-header"> <a target="_blank" :href="job.direct_link">{{ job.role }} </a></span>
          <span class="row text-subtitle1">{{ job.company }}</span>
        </div>
        </div>
        <div class="q-pr-lg col-12 col-md-4">
          <q-icon color="primary" size="17px" class="q-mx-xs" name="event" /> <span> {{ job.datef }}</span>
          <span class="row text-body2"><a target="_blank" :href="job.jobsite_link"> {{ job.jobsite }} </a></span>
        </div>
        <div class="col-12 col-md-4">
          <q-chip
            v-for="(chip, index) in job.tags"
            :key="'c'+index"
            class="q-pa-md"
            size="15px"
            @remove="removeIgnoreChip(ignoreIndex)"
            color="green-9"
            text-color="white"
          >
          {{ chip }}
        </q-chip>
        </div>
      </div>
    </q-card>

    <q-btn color="primary" glossy class="q-mx-xs q-my-lg" @click="moreResults">More Results</q-btn>

    <q-page-scroller position="bottom-right" :scroll-offset="150" :offset="[18, 18]">
      <q-btn fab icon="keyboard_arrow_up" color="primary" />
    </q-page-scroller>
    <div class="q-ma-lg q-pa-lg"></div>
  </q-page>
</template>

<script>
export default {
  data: () => ({
    jobs: [],
    filteredJobs: [],
    includeChips: [],
    ignoreChips: [],
    includeChip: "",
    ignoreChip: "",
    loading: false,
    currentPage: 1,
    maxPages: 0,
    totalFilteredJobs: null,
    resultsPerPage: 40
  }),
  async mounted() {
    this.loading = true;
    try {
      await this.$auth.checkTokens();
      await this.retrieveFilters()
    }
    catch {
      console.log('There was an issue mounting the page.')
    }
    await this.getJobs();
    this.loading = false;
  },
  methods: {
    async getJobs() {
      const jobList = await this.$auth.axios({ url: "jobs" });
      this.jobs = jobList.data;
      this.filter();
    },
    filter() {
      this.filteredJobs = JSON.parse(JSON.stringify(this.jobs));
      this.includeChips.forEach((chip) => {
        this.filteredJobs = this.filteredJobs.filter((job) => {
          return job.role.toLowerCase().includes(chip.toLowerCase());
        });
      });
      this.ignoreChips.forEach((chip) => {
        this.filteredJobs = this.filteredJobs.filter((job) => {
          return !job.role.toLowerCase().includes(chip.toLowerCase());
        });
      });
      this.totalFilteredJobs =  this.filteredJobs.length
      const startIndex = (this.currentPage - 1) * this.resultsPerPage
      const endIndex =  (this.currentPage - 1) * this.resultsPerPage + this.resultsPerPage
      this.maxPages = parseInt(this.filteredJobs.length / this.resultsPerPage)+1;
      this.filteredJobs = this.filteredJobs.slice(startIndex, endIndex)
    },
    submitIncludeChip() {
      if (this.includeChip) {
        this.includeChips = [
          ...this.includeChips,
          ...this.includeChip.split(","),
        ];
      }
      this.includeChip = "";
      this.filter();
    },
    submitIgnoreChip() {
      if (this.ignoreChip) {
        this.ignoreChips = [...this.ignoreChips, ...this.ignoreChip.split(",")];
      }
      this.ignoreChip = "";
      this.filter();
    },
    removeIncludeChip(chipIndex) {
      this.includeChips.splice(chipIndex, 1);
      this.filter();
    },
    removeIgnoreChip(chipIndex) {
      this.ignoreChips.splice(chipIndex, 1);
      this.filter();
    },
    async saveFilters() {
      if (!this.$auth.user()) {
        this.$router.push('/login')
        return
      }
      try {
        await this.$auth.axios({ url: '/profile/', data: {
          includeChips: this.includeChips,
          ignoreChips: this.ignoreChips
        }, method: 'POST' })
        this.$q.notify({ message: "Filters saved" });
      }
      catch {
        this.$q.notify({
          message: "There was a problem saving your filters",
          color: "red-6",
          icon: "error",
        });
      }
    },
    async retrieveFilters() {
      try {
        const response = await this.$auth.axios({ url: '/profile/', method: 'GET' })
        this.includeChips = response.data.include_chips
        this.ignoreChips = response.data.ignore_chips
      }
      catch {
        console.log('There was a problem retrieving the saved filters. Are you logged in?')
      }
    },
    moreResults() {
      this.resultsPerPage += this.resultsPerPage
      this.filter();
    }
  },
  computed: {
    authUserName() {
      const user = this.$auth.user();
      if (user) {
        return user.first_name;
      }
    },
    resultsPerPageDisplay() {
      return this.totalFilteredJobs <= this.resultsPerPage ? this.totalFilteredJobs : this.resultsPerPage
    }
  },
};
</script>


<style lang="scss" scoped>

  a {
    color: black;
    &:hover {
      color: rgb(75, 75, 75);
    }
  }
</style>