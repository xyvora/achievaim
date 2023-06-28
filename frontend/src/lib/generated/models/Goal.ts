/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { DaysOfWeek } from './DaysOfWeek';
import type { RepeatsEvery } from './RepeatsEvery';

/**
 * Document Mapping class.
 *
 * Fields:
 *
 * - `id` - MongoDB document ObjectID "_id" field.
 * Mapped to the PydanticObjectId class
 *
 * Inherited from:
 *
 * - Pydantic BaseModel
 * - [UpdateMethods](https://roman-right.github.io/beanie/api/interfaces/#aggregatemethods)
 */
export type Goal = {
  _id?: string;
  name: string;
  duration: number;
  daysOfWeek: DaysOfWeek;
  repeatsEvery: RepeatsEvery;
  progress: number;
};
