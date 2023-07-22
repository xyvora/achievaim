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

export interface User {
  username: string | null;
  avatar: string | null;
  firstName: string | null;
  lastName: string | null;
  country: string | null;
  password: string | null;
}

export interface UserLogin {
  userName?: string;
  password?: string;
}

export interface AccessToken {
  access_token: string;
  token_type: string;
}
