/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { DaysOfWeek } from './DaysOfWeek';

export type GoalCreate = {
  goal?: string;
  specific?: string;
  measurable?: string;
  attainable?: string;
  relevant?: string;
  date_for_achievement?: string;
  days_of_week?: DaysOfWeek;
  time_of_day?: string;
  progress?: number;
};
