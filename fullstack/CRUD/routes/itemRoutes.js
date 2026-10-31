const express = require('express');
const router = express.Router();

const Item = require('../models/Item');

// POST - Add a new item
router.post('/', async (req, res) => {
    try {
        const newItem = new Item({
            name: req.body.name,
            description: req.body.description
        });

        const savedItem = await newItem.save();

        res.status(201).json(savedItem);

    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// GET - Fetch all items
router.get('/', async (req, res) => {
    try {
        const items = await Item.find();

        res.status(200).json(items);

    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// PUT - Update an item
router.put('/:id', async (req, res) => {
    try {
        const updatedItem = await Item.findByIdAndUpdate(
            req.params.id,
            {
                name: req.body.name,
                description: req.body.description
            },
            { new: true, runValidators: true }
        );

        if (!updatedItem) {
            return res.status(404).json({ message: 'Item not found' });
        }

        res.status(200).json(updatedItem);

    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// DELETE - Delete an item
router.delete('/:id', async (req, res) => {
    try {
        const deletedItem = await Item.findByIdAndDelete(req.params.id);

        if (!deletedItem) {
            return res.status(404).json({ message: 'Item not found' });
        }

        res.status(200).json({ message: 'Item deleted successfully' });

    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

module.exports = router;