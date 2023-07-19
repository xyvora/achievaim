import { axiosInstance } from '$lib/axios-config';
import type { AccessToken, UserLogin } from '$lib/types';

/* export const createGoal = async (goal: GoalBase) => {
  try {
    const response = await axiosInstance.post('/goal', goal);
    if (response.status == 200) {
      return response.data;
    } else {
      throw new Error(response.statusText);
    }
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const getGoals = async () => {
  try {
    const response = await axiosInstance.get('/goal');
    if (response.status == 200) {
      return response.data;
    } else {
      throw new Error(response.statusText);
    }
  } catch (error) {
    console.error(error);
    throw error;
  }
}; */

export const login = async (loginInfo: UserLogin): Promise<AccessToken> => {
  if (loginInfo.userName == null || loginInfo.password == null) {
    throw new Error('A user name and password are required');
  }
  const formData = new FormData();
  formData.append('username', loginInfo.userName);
  formData.append('password', loginInfo.password);
  try {
    const response = await axiosInstance.post('/login/access-token', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    if (response.status == 200) {
      return response.data;
    } else {
      throw new Error(response.statusText);
    }
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
