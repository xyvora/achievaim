/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { DaysOfWeek } from './DaysOfWeek';
import type { RepeatsEvery } from './RepeatsEvery';

/**
 * A Pydantic model that provides a base configuration for conveting between camel and snake case.
 *
 * If another Pydantic model inherit from this class it will get the ability to do this conversion
 * between camel and snake case without having to add the configuration to the new model.
 */
export type GoalUpdate = {
  name: string;
  duration: number;
  daysOfWeek: DaysOfWeek;
  repeatsEvery: RepeatsEvery;
  progress: number;
  id: string;
};
