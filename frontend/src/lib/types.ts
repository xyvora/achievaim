export interface Goal {
  name: string;
  details: string;
  date: Date;
  days: number[];
  editing: boolean;
}

export interface Goals {
  active: Goal[];
  completed: Goal[];
}

export interface UserLogin {
  userName?: string;
  password?: string;
}

export interface AccessToken {
  access_token: string;
  token_type: string;
}
