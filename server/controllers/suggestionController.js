const openai = require("../services/openai");

exports.generateSuggestions = async (req, res) => {
  try {
    const { input } = req.body;

    // Make a call to the OpenAI GPT API to generate suggestions based on the input
    const response = await openai.generateSuggestions(input);

    res.status(200).json(response);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Internal server error" });
  }
};
