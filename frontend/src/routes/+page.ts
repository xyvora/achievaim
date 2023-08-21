import { isValidToken } from '$lib/api';
import { accessToken } from '$lib/stores/stores';

export async function load() {
  const isAuthenticated = await isValidToken();
  if (!isAuthenticated) {
    accessToken.set(null);
  }
  return {
    isAuthenticated,
  };
}
