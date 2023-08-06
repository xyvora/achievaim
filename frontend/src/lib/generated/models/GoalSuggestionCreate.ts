/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { GoalInfo } from './GoalInfo';

export type GoalSuggestionCreate = {
  goal: string;
  model?: string | null;
  temperature?: number | null;
  specific?: GoalInfo | null;
  measurable?: GoalInfo | null;
  achievable?: GoalInfo | null;
  relevant?: GoalInfo | null;
  time_bound?: GoalInfo | null;
};
