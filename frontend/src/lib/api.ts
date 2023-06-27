import { axiosInstance } from '$lib/axios-config';
import type { Goal } from '$lib/generated';
import type { GoalBase } from '$lib/generated';
// import type { GoalUpdate } from '$lib/generated';

export const createGoal = async (goal: GoalBase): Goal => {
  try {
    const response = await axiosInstance.post('/goal', { goal });
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const getGoals = async (): Goal[] => {
  try {
    const response = await axiosInstance.get('/goal');
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

/* export const updateGoal = async (goal) => {
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
}; */
