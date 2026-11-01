
<script setup>
import { ref, computed } from 'vue'
import { useApplicationStore } from './stores/application'

const store = useApplicationStore()
const step = ref(1)

// Age validation
const isAdult = computed(() => {
  const dob = new Date(store.personal.dob)
  const today = new Date()
  let age = today.getFullYear() - dob.getFullYear()

  if (
    today.getMonth() < dob.getMonth() ||
    (today.getMonth() === dob.getMonth() &&
     today.getDate() < dob.getDate())
  ) age--

  return store.personal.dob && age >= 18
})

// Step validations
const valid1 = computed(() =>
  store.personal.name.trim() &&
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(store.personal.email) &&
  /^\d{10}$/.test(store.personal.phone) &&
  isAdult.value
)

const valid2 = computed(() =>
  store.education.degree &&
  store.education.institution.trim() &&
  Number(store.education.year) >= 1900 &&
  Number(store.education.year) <= new Date().getFullYear()
)

const valid3 = computed(() =>
  store.experience.every(e =>
    e.company.trim() &&
    e.role.trim() &&
    (!e.start || !e.end || e.end > e.start)
  )
)

const canNext = computed(() => {
  if (step.value === 1) return valid1.value
  if (step.value === 2) return valid2.value
  if (step.value === 3) return valid3.value
})

function addExperience() {
  store.experience.push({
    company: '',
    role: '',
    start: '',
    end: ''
  })
}

function removeExperience(index) {
  store.experience.splice(index, 1)
}

function next() {
  if (canNext.value) step.value++
}

function back() {
  if (step.value > 1) step.value--
}

async function submit() {
  const res = await fetch('http://localhost:5000/api/applications', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(store.$state)
  })

  if (res.ok) alert('Application submitted!')
  else alert('Submission failed')
}
</script>

<template>
  <h2>Job Application Form</h2>
  <p>Step {{ step }} of 4</p>

  <!-- STEP 1 -->
  <div v-if="step === 1">
    <h3>Personal Details</h3>

    <input v-model="store.personal.name" placeholder="Name">
    <input v-model="store.personal.email" placeholder="Email">
    <input v-model="store.personal.phone" placeholder="Phone">
    <input v-model="store.personal.dob" type="date">
  </div>

  <!-- STEP 2 -->
  <div v-if="step === 2">
    <h3>Education</h3>

    <input v-model="store.education.degree" placeholder="Degree">
    <input v-model="store.education.institution" placeholder="Institution">
    <input v-model="store.education.year" type="number" placeholder="Passing Year">
  </div>

  <!-- STEP 3 -->
  <div v-if="step === 3">
    <h3>Work Experience</h3>

    <button @click="addExperience">Add Work Experience</button>

    <div v-for="(job, index) in store.experience" :key="index">
      <h4>Experience {{ index + 1 }}</h4>

      <input v-model="job.company" placeholder="Company">
      <input v-model="job.role" placeholder="Role">
      <input v-model="job.start" type="date">
      <input v-model="job.end" type="date">

      <button @click="removeExperience(index)">Remove</button>
    </div>
  </div>

  <!-- STEP 4 -->
  <div v-if="step === 4">
    <h3>Review Application</h3>

    <h4>Personal Details</h4>
    <p>{{ store.personal }}</p>

    <h4>Education</h4>
    <p>{{ store.education }}</p>

    <h4>Work Experience</h4>
    <div v-for="job in store.experience">
      <p>{{ job }}</p>
    </div>

    <button @click="submit">Submit Application</button>
  </div>

  <!-- NAVIGATION -->
  <button v-if="step > 1" @click="back">Back</button>

  <button
    v-if="step < 4"
    @click="next"
    :disabled="!canNext"
  >
    Next
  </button>
</template>
