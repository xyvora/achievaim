import { isValidToken } from '$lib/api';
import { accessToken } from '$lib/stores/stores';

export const load = async ({ params }) => {
  const isAuthenticated = await isValidToken();
  if (!isAuthenticated) {
    accessToken.set(null);
  }
  return {
    isAuthenticated,
    goalId: params.id,
  };
};
