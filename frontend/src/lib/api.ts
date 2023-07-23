import { AxiosError } from 'axios';
import { axiosInstance } from '$lib/axios-config';
import type { UserCreate, UserNoPassword } from '$lib/generated';
import type { AccessToken, UserLogin } from '$lib/types';
import { LoginError } from '$lib/errors';
import { accessToken } from '$lib/stores/stores';

function authHeaders() {
  let token: AccessToken | null;
  accessToken.subscribe((value: AccessToken | null) => (token = value));

  return {
    headers: {
      Authorization: `Bearer ${token.access_token}`
    }
  };
}

export const createUser = async (user: UserCreate): Promise<UserNoPassword> => {
  // TODO: Better handle errors
  const response = await axiosInstance.post('/user', user);

  if (response.status === 200) {
    return response.data;
  } else {
    throw new Error(response.statusText);
  }
};

export const getMe = async (): Promise<UserNoPassword> => {
  // TODO: Better handle errors
  const response = await axiosInstance.get('/user/me', authHeaders());

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
  try {
    const response = await axiosInstance.post('/login/access-token', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    if (response.status === 200) {
      return response.data;
    } else {
      throw new LoginError(response.statusText);
    }
  } catch (error) {
    if (error instanceof AxiosError) {
      if (
        error.response !== undefined &&
        error.response.data !== undefined &&
        error.response.data.detail !== undefined
      ) {
        throw new LoginError(error.response.data.detail);
      }
    }
    throw error;
  }
};
