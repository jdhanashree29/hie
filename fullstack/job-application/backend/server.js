
const express = require('express')
const mongoose = require('mongoose')
const cors = require('cors')

const app = express()

app.use(cors())
app.use(express.json())

mongoose.connect('mongodb://127.0.0.1:27017/jobDB')
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err))

// Schema
const Application = mongoose.model('Application', {
  personal: Object,
  education: Object,
  experience: Array
})

// POST - Save application
app.post('/api/applications', async (req, res) => {
  try {
    const application = new Application(req.body)
    await application.save()
    res.status(201).json({ message: 'Application saved' })
  } catch (err) {
    res.status(500).json({ error: err.message })
  }
})

// GET - Display applications
app.get('/api/applications', async (req, res) => {
  const applications = await Application.find()
  res.json(applications)
})

app.listen(5000, () => {
  console.log('Server running on port 5000')
})


