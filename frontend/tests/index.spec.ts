import { expect, test } from '@playwright/test';
import { v4 as uuidv4 } from 'uuid';

test('page loads', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('#navbar')).toBeVisible();
});

test('navbar link is active', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('link', { name: /home/ })).toHaveClass('rounded bg-white');
});

test('user name is required', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('#user-name')).toBeVisible();
  await page.locator('#login-button').click();
  await expect(page.locator('#user-name-error')).toBeVisible();
});

test('password is required', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('#password')).toBeVisible();
  await page.locator('#login-button').click();
  await expect(page.locator('#password-error')).toBeVisible();
});

test('end to end sign in', async ({ page }) => {
  const userName = uuidv4();
  const password = 'mypassword';
  const goal = 'Some Goal';

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
  await expect(page.locator('#btn-log-out')).toBeVisible();
  await page.locator('#btn-log-out').click();
  await expect(page).toHaveURL('/');
  await page.locator('#user-name').fill(userName);
  await page.locator('#password').fill(password);
  await page.locator('#login-button').click();
  await expect(page).toHaveURL('/');
  await expect(page.locator('#login-button')).not.toBeVisible();
  await expect(page.getByText('No active goals')).toBeVisible();
  await expect(page.getByLabel('account settings')).toBeVisible();
  await page.getByLabel('create goal').click();
  await expect(page).toHaveURL('/create-goals');
  await page.locator('#goal').fill(goal);
  await page.locator('#save-goal-button').click();
  await expect(page).toHaveURL('/', { timeout: 10000 });
  await expect(page.getByText(goal)).toBeVisible();

  await page.getByLabel('account settings').click();
  await expect(page.locator('#btn-delete')).toBeVisible();
  await page.locator('#btn-delete').click();
  await expect(page.locator('#btn-delete')).toBeVisible();
  page.once('dialog', async (dialog) => {
    await dialog.accept();
  });
  await page.locator('#btn-delete').click();
  await expect(page).toHaveURL('/');
});

test('end to end sign in invalid user', async ({ page }) => {
  const userName = uuidv4();
  const password = 'mypassword';

  await page.goto('/');
  await page.locator('#user-name').fill(userName);
  await page.locator('#password').fill(password);
  await page.locator('#login-button').click();
  await expect(page.locator('#generic-error')).toBeVisible();
  await expect(page.locator('#generic-error')).toHaveText('Incorrect user name or password');
});
