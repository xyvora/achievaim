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

accessToken.subscribe((value: AccessToken | null) => {
  if (!browser) {
    return null;
  }

  if (value) {
    localStorage.setItem('accessToken', JSON.stringify(value));
  } else {
    localStorage.removeItem('accessToken');
  }
});
