/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { DaysOfWeekOutput } from './DaysOfWeekOutput';
import type { GoalStatus } from './GoalStatus';

export type GoalOutput = {
  goal: string;
  specific: string | null;
  measurable: string | null;
  attainable: string | null;
  relevant: string | null;
  time_bound: string | null;
  date_for_achievement: string | null;
  days_of_week: DaysOfWeekOutput | null;
  time_of_day: string | null;
  progress: number | null;
  status: GoalStatus;
  id: string;
};
