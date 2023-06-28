import type { PageLoad } from './$types';
import { getGoals } from '$lib/api';
import type { Goal } from '$lib/generated';

export const load: PageLoad = async () => {
  const goals: Goal[] = await getGoals();

  return { goals };
};
