import { writable } from 'svelte/store';
import { browser } from '$app/environment';
import type { AccessToken } from '$lib/types';

const getToken = (): AccessToken | null => {
  if (!browser) {
    return null;
  }

  const token = localStorage.getItem('accessToken');
  if (token) {
    return JSON.parse(token) as AccessToken;
  }
  return null;
};

export const accessToken = writable<AccessToken | null>(browser ? getToken() : null);
export const isLoggedIn = writable<boolean>(browser && getToken() !== null ? true : false);

accessToken.subscribe((value: AccessToken | null) => {
  if (!browser) {
    return null;
  }

  if (value) {
    localStorage.setItem('accessToken', JSON.stringify(value));
  } else {
    localStorage.removeItem('accessToken');
  }

  isLoggedIn.set(value !== null);
});

isLoggedIn.subscribe((value: boolean) => {
  if (!browser) {
    return false;
  }

  if (value === true) {
    localStorage.setItem('isLoggedIn', 'true');
  }

  localStorage.setItem('isLoggedIn', 'false');
});

export const isLoading = writable<boolean>(false);

isLoading.subscribe((value: boolean) => {
  return value;
});

export const showToast = writable<boolean>(false);

showToast.subscribe((value: boolean) => {
  return value;
});

export const toastMessage = writable<string>();

toastMessage.subscribe((value: string) => {
  return value;
});

function delay(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export async function setToast(message: string, timeout = 5000) {
  toastMessage.set(message);
  showToast.set(true);
  await delay(timeout);
  showToast.set(false);
}
