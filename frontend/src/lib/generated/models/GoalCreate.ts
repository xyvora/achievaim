/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { DaysOfWeekInput } from './DaysOfWeekInput';

export type GoalCreate = {
  goal?: string | null;
  specific?: string | null;
  measurable?: string | null;
  attainable?: string | null;
  relevant?: string | null;
  time_bound?: string | null;
  date_for_achievement?: string | null;
  days_of_week?: DaysOfWeekInput | null;
  time_of_day?: string | null;
  progress?: number | null;
};
