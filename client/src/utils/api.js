// client/src/utils/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
});

export const createGoal = async (goal) => {
  try {
    const response = await api.post('/goals', { goal });
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const getGoals = async () => {
  try {
    const response = await api.get('/goals');
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const updateGoal = async (goal) => {
  try {
    const response = await api.put(`/goals/${goal._id}`, goal);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const generateSuggestions = async (input) => {
  try {
    const response = await api.post('/suggestions', { input });
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};
