import type { AxiosError, AxiosRequestConfig, AxiosResponse } from 'axios';
import { axiosInstance } from '$lib/axios-config';
import type {
  GoalOutput,
  GoalCreate,
  GoalSuggestionCreate,
  PasswordReset,
  SmartGoal,
  UserCreate,
  UserNoPassword,
  UserUpdateMe,
} from '$lib/generated';
import type { AccessToken, UserLogin } from '$lib/types';
import { accessToken } from '$lib/stores/stores';

// eslint-disable-next-line @typescript-eslint/no-explicit-any
async function authHeaders(): Promise<AxiosRequestConfig<any>> {
  const token: AccessToken | null = await new Promise<AccessToken | null>((resolve) => {
    accessToken.subscribe((value: AccessToken | null) => resolve(value));
  });

  if (token) {
    return {
      headers: {
        Authorization: `Bearer ${token.access_token}`,
      },
    };
  }

  throw new Error('No access token found');
}

export const createOpenAiSuggestion = async (payload: GoalSuggestionCreate): Promise<SmartGoal> => {
  const headers = await authHeaders();
  // Give a long timeout here becausee OpenAI is SLOW
  const response = await axiosInstance.post('/goal/openai-goal', payload, {
    ...headers,
    timeout: 30000,
  });

  if (response.status === 200) {
    return response.data;
  }

  throw new Error(response.statusText);
};

export const createGoal = async (payload: GoalCreate): Promise<GoalOutput[]> => {
  const headers = await authHeaders();
  const response = await axiosInstance.post('/goal', payload, headers);

  if (response.status === 200) {
    return response.data;
  }

  throw new Error(response.statusText);
};

export const createUser = async (user: UserCreate): Promise<UserNoPassword> => {
  // TODO: Better handle errors
  const response = await axiosInstance.post('/user', user);

  if (response.status === 200) {
    return response.data;
  } else {
    throw new Error(response.statusText);
  }
};

export const deleteGoal = async (goalId: string) => {
  // TODO: Better handle errors
  const headers = await authHeaders();
  const response = await axiosInstance.delete(`/goal/${goalId}`, headers);

  if (response.status !== 204) {
    throw new Error(response.statusText);
  }
};

export const deleteMe = async () => {
  // TODO: Better handle errors
  const headers = await authHeaders();
  const response = await axiosInstance.delete('/user/me', headers);

  if (response.status !== 204) {
    throw new Error(response.statusText);
  }
};

export const forgotPassword = async (payload: PasswordReset): Promise<UserNoPassword> => {
  // TODO: Better handle errors
  const response = await axiosInstance.patch('/user/forgot-password', payload);

  if (response.status === 200) {
    return response.data;
  } else {
    throw new Error(response.statusText);
  }
};

export const getGoals = async (): Promise<GoalOutput[] | null> => {
  // TODO: Better handle errors
  const headers = await authHeaders();
  return await axiosInstance.get('/goal', headers);
};

export const getMe = async (): Promise<UserNoPassword> => {
  // TODO: Better handle errors
  const headers = await authHeaders();
  const response = await axiosInstance.get('/user/me', headers);

  if (response.status === 200) {
    return response.data;
  } else {
    throw new Error(response.statusText);
  }
};

export const login = async (loginInfo: UserLogin): Promise<AccessToken> => {
  if (loginInfo.userName == null || loginInfo.password == null) {
    throw new Error('A user name and password are required');
  }
  const formData = new FormData();
  formData.append('username', loginInfo.userName);
  formData.append('password', loginInfo.password);
  const response = await axiosInstance.post('/login/access-token', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });

  if (response.status === 200) {
    return response.data;
  }

  throw response;
};

export const updateGoal = async (payload: GoalOutput): Promise<GoalOutput[]> => {
  // TODO: Better handle errors
  const headers = await authHeaders();
  const response = await axiosInstance.put('/goal', payload, headers);

  if (response.status === 200) {
    return response.data;
  } else {
    throw new Error(response.statusText);
  }
};

export const updateMe = async (payload: UserUpdateMe): Promise<UserNoPassword> => {
  // TODO: Better handle errors
  const headers = await authHeaders();
  const response = await axiosInstance.put('/user/me', payload, headers);

  if (response.status === 200) {
    return response.data;
  } else {
    throw new Error(response.statusText);
  }
};
