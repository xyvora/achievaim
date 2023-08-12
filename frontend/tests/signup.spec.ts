import { expect, test } from '@playwright/test';
import { v4 as uuidv4 } from 'uuid';

test('page loads', async ({ page }) => {
  await page.goto('/signup');
  await expect(page.locator('#navbar')).toBeVisible();
});

test('first name is required', async ({ page }) => {
  await page.goto('/signup');
  await expect(page.locator('#first-name')).toBeVisible();
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#first-name-error')).toBeVisible();
});

test('last name is required', async ({ page }) => {
  await page.goto('/signup');
  await expect(page.locator('#last-name')).toBeVisible();
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#last-name-error')).toBeVisible();
});

test('user name is required', async ({ page }) => {
  await page.goto('/signup');
  await expect(page.locator('#user-name')).toBeVisible();
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#user-name-error')).toBeVisible();
});

test('security question is required', async ({ page }) => {
  await page.goto('/signup');
  await expect(page.locator('#security-question-answer')).toBeVisible();
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#security-question-answer')).toBeVisible();
});

test('password is required', async ({ page }) => {
  await page.goto('/signup');
  await expect(page.locator('#password')).toBeVisible();
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#password-error')).toBeVisible();
});

test('password mismatch', async ({ page }) => {
  await page.goto('/signup');
  await expect(page.locator('#password')).toBeVisible();
  await expect(page.locator('#verify-password')).toBeVisible();
  await page.locator('#password').fill('a');
  await page.locator('#verify-password').fill('b');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#password-verify-error')).toBeVisible();
});

test('end to end signup', async ({ page }) => {
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
  await expect(page.locator('#toast-message')).toBeVisible();
  await expect(page.locator('#btn-sign-up')).not.toBeVisible();
  await expect(page.locator('#btn-log-out')).toBeVisible();
  await expect(page.locator('#btn-delete')).toBeVisible();
  page.once('dialog', async (dialog) => {
    await dialog.accept();
  });
  await page.locator('#btn-delete').click();
  await expect(page).toHaveURL('/');
});
