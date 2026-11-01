const express = require('express');
const mongoose = require('mongoose');

const app = express();

app.use(express.json());

// MongoDB connection
mongoose.connect('mongodb://127.0.0.1:27017/crudDB')
    .then(() => console.log("MongoDB Connected"))
    .catch(err => console.log(err));

// Import model
const Item = require('./models/Item');

// CREATE
app.post('/items', async (req, res) => {
    const item = await Item.create(req.body);
    res.status(201).json(item);
});

// READ ALL
app.get('/items', async (req, res) => {
    const items = await Item.find();
    res.json(items);
});

// READ BY ID
app.get('/items/:id', async (req, res) => {
    const item = await Item.findById(req.params.id);
    if (!item) return res.status(404).json({ message: "Item not found" });
    res.json(item);
});

// UPDATE
app.put('/items/:id', async (req, res) => {
    const item = await Item.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true, runValidators: true }
    );
    if (!item) return res.status(404).json({ message: "Item not found" });
    res.json(item);
});

// DELETE
app.delete('/items/:id', async (req, res) => {
    const item = await Item.findByIdAndDelete(req.params.id);
    if (!item) return res.status(404).json({ message: "Item not found" });
    res.json({ message: "Item deleted successfully" });
});

// Start server
app.listen(3000, () => {
    console.log("Server running on port 3000");
});