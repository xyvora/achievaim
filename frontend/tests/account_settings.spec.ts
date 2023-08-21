import { expect, test } from '@playwright/test';
import { v4 as uuidv4 } from 'uuid';

test('page loads', async ({ page }) => {
  const userName = uuidv4();
  const password = 'mypassword';

  await page.goto('/');
  await expect(
    page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }),
  ).toBeVisible();
  await page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }).click();
  await page.locator('#first-name').fill('Imma');
  await page.locator('#last-name').fill('User');
  await page.locator('#user-name').fill(userName);
  await page.locator('#security-question-answer').fill('my answer');
  await page.locator('#password').fill(password);
  await page.locator('#verify-password').fill(password);
  await page.locator('#btn-sign-up').click();

  await page.goto('/account-settings');
  await expect(page.locator('#navbar')).toBeVisible();
});

test('first name required', async ({ page }) => {
  const userName = uuidv4();
  const password = 'mypassword';

  await page.goto('/');
  await expect(
    page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }),
  ).toBeVisible();
  await page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }).click();
  await page.locator('#first-name').fill('Imma');
  await page.locator('#last-name').fill('User');
  await page.locator('#user-name').fill(userName);
  await page.locator('#security-question-answer').fill('my answer');
  await page.locator('#password').fill(password);
  await page.locator('#verify-password').fill(password);
  await page.locator('#btn-sign-up').click();

  await page.goto('/account-settings');
  await page.locator('#first-name').fill('');
  await page.locator('#btn-save').click();
  await expect(page.locator('#first-name-error')).toBeVisible();
});

test('last name required', async ({ page }) => {
  const userName = uuidv4();
  const password = 'mypassword';

  await page.goto('/');
  await expect(
    page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }),
  ).toBeVisible();
  await page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }).click();
  await page.locator('#first-name').fill('Imma');
  await page.locator('#last-name').fill('User');
  await page.locator('#user-name').fill(userName);
  await page.locator('#security-question-answer').fill('my answer');
  await page.locator('#password').fill(password);
  await page.locator('#verify-password').fill(password);
  await page.locator('#btn-sign-up').click();
  await expect(page).toHaveURL('/account-settings');
  await page.locator('#last-name').fill('');
  await page.locator('#btn-save').click();
  await expect(page.locator('#last-name-error')).toBeVisible();
});

test('user name required', async ({ page }) => {
  const userName = uuidv4();
  const password = 'mypassword';

  await page.goto('/');
  await expect(
    page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }),
  ).toBeVisible();
  await page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }).click();
  await page.locator('#first-name').fill('Imma');
  await page.locator('#last-name').fill('User');
  await page.locator('#user-name').fill(userName);
  await page.locator('#security-question-answer').fill('my answer');
  await page.locator('#password').fill(password);
  await page.locator('#verify-password').fill(password);
  await page.locator('#btn-sign-up').click();
  await expect(page).toHaveURL('/account-settings');
  await page.locator('#user-name').fill('');
  await page.locator('#btn-save').click();
  await expect(page.locator('#user-name-error')).toBeVisible();
});

test('password required', async ({ page }) => {
  const userName = uuidv4();
  const password = 'mypassword';

  await page.goto('/');
  await expect(
    page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }),
  ).toBeVisible();
  await page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }).click();
  await page.locator('#first-name').fill('Imma');
  await page.locator('#last-name').fill('User');
  await page.locator('#user-name').fill(userName);
  await page.locator('#security-question-answer').fill('my answer');
  await page.locator('#password').fill(password);
  await page.locator('#verify-password').fill(password);
  await page.locator('#btn-sign-up').click();
  await expect(page).toHaveURL('/account-settings');
  await page.locator('#password').fill('');
  await page.locator('#btn-save').click();
  await expect(page.locator('#password-error')).toBeVisible();
});

test('passwords match error', async ({ page }) => {
  const userName = uuidv4();
  const password = 'mypassword';

  await page.goto('/');
  await expect(
    page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }),
  ).toBeVisible();
  await page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }).click();
  await page.locator('#first-name').fill('Imma');
  await page.locator('#last-name').fill('User');
  await page.locator('#user-name').fill(userName);
  await page.locator('#security-question-answer').fill('my answer');
  await page.locator('#password').fill(password);
  await page.locator('#verify-password').fill(password);
  await page.locator('#btn-sign-up').click();
  await expect(page).toHaveURL('/account-settings');
  await page.locator('#password').fill('a');
  await page.locator('#verify-password').fill('b');
  await page.locator('#btn-save').click();
  await expect(page.locator('#password-verify-error')).toBeVisible();
});

test('not logged in buttons', async ({ page }) => {
  await page.goto('/account-settings');
  await expect(page.locator('#btn-sign-up')).toBeVisible();
  await expect(page.locator('#btn-save')).not.toBeVisible();
  await expect(page.locator('#btn-log-out')).not.toBeVisible();
  await expect(page.locator('#btn-delete')).not.toBeVisible();
});

test('not logged in', async ({ page }) => {
  await page.goto('/account-settings');
  await expect(page).toHaveURL('/');
});

test('end to end update user info', async ({ page }) => {
  const userName = uuidv4();
  const password = 'mypassword';

  await page.goto('/');
  await expect(
    page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }),
  ).toBeVisible();
  await page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }).click();
  await expect(page.locator('#first-name')).toBeVisible();
  await expect(page.locator('#last-name')).toBeVisible();
  await expect(page.locator('#user-name')).toBeVisible();
  await expect(page.locator('#security-question-answer')).toBeVisible();
  await expect(page.locator('#password')).toBeVisible();
  await expect(page.locator('#verify-password')).toBeVisible();
  await expect(page.locator('#btn-sign-up')).toBeVisible();
  await page.locator('#first-name').fill('Imma');
  await page.locator('#last-name').fill('User');
  await page.locator('#user-name').fill(userName);
  await page.locator('#security-question-answer').fill('my answer');
  await page.locator('#password').fill(password);
  await page.locator('#verify-password').fill(password);
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#btn-sign-up')).not.toBeVisible();
  await expect(page.locator('#btn-save')).toBeVisible();
  await expect(page.locator('#btn-log-out')).toBeVisible();
  await expect(page.locator('#btn-delete')).toBeVisible();
  await page.locator('#last-name').fill('Person');
  await page.locator('#password').fill(password);
  await page.locator('#verify-password').fill(password);
  await page.locator('#btn-save').click();
  await expect(page.locator('#last-name')).toHaveValue('Person');
  page.once('dialog', async (dialog) => {
    await dialog.accept();
  });
  await page.locator('#btn-delete').click();
  await expect(page).toHaveURL('/');
});
