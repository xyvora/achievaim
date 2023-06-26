const Goal = require('../models/Goal');

exports.createGoal = async (req, res) => {
  try {
    const { goal } = req.body;
    const newGoal = await Goal.create({ name: goal });
    res.status(201).json(newGoal);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
};

exports.getGoals = async (req, res) => {
  try {
    const goals = await Goal.find();
    res.status(200).json(goals);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
};

exports.updateGoal = async (req, res) => {
  try {
    const { id } = req.params;
    const { duration, daysOfWeek, repeatsEvery, progress } = req.body;
    const updatedGoal = await Goal.findByIdAndUpdate(
      id,
      { duration, daysOfWeek, repeatsEvery, progress },
      { new: true }
    );
    res.status(200).json(updatedGoal);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
};
