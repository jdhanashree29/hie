const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

const app = express();

// Middleware
app.use(express.json());
app.use(cors());

// Import Model
const itemRoutes = require('./routes/itemRoutes');

// Routes
app.use('/api/items', itemRoutes);

// MongoDB Connection
mongoose.connect(process.env.MONGODB_URI)
.then(() => {
    console.log('MongoDB Connected Successfully');
})
.catch(err => {
    console.log('MongoDB Connection Error:', err);
});

// Server
const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});