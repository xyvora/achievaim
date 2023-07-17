/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { DaysOfWeek } from './DaysOfWeek';
import type { RepeatsEvery } from './RepeatsEvery';

export type GoalCreate = {
  name: string;
  duration?: number;
  days_of_week?: DaysOfWeek;
  repeats_every?: RepeatsEvery;
  progress?: number;
};
