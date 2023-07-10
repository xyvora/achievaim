export interface Goal {
  name: string;
  details: string;
  date: Date;
  days: number[];
  editing: boolean;
}

export interface Goals {
  future: Goal[];
  inProgress: Goal[];
  completed: Goal[];
}
