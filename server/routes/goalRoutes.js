const express = require('express');
const router = express.Router();
const goalController = require('../controllers/goalController');

router.post('/', goalController.createGoal);
router.get('/', goalController.getGoals);
router.put('/:id', goalController.updateGoal);

module.exports = router;
