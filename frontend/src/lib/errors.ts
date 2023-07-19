export class LoginError extends Error {
  detail?: string;

  constructor(message: string) {
    super(message);
    this.name = 'LoginError';
  }
}
