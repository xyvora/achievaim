const mongoose = require("mongoose");

const goalSchema = new mongoose.Schema({
  name: { type: String, required: true },
  duration: { type: String, required: true },
  daysOfWeek: {
    monday: { type: Boolean, default: false },
    tuesday: { type: Boolean, default: false },
    wednesday: { type: Boolean, default: false },
    thursday: { type: Boolean, default: false },
    friday: { type: Boolean, default: false },
    saturday: { type: Boolean, default: false },
    sunday: { type: Boolean, default: false },
  },
  repeatsEvery: { type: String, required: true },
  progress: { type: Number, required: true },
});

module.exports = mongoose.model("Goal", goalSchema);
