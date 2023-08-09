import { expect, test } from '@playwright/test';
import { v4 as uuidv4 } from 'uuid';

test('page loads', async ({ page }) => {
  await page.goto('/forgot-password');
  await expect(page.locator('#navbar')).toBeVisible();
});

test('user name is required', async ({ page }) => {
  await page.goto('/forgot-password');
  await expect(page.locator('#user-name')).toBeVisible();
  await page.locator('#btn-reset').click();
  await expect(page.locator('#user-name-error')).toBeVisible();
});

test('security answer is required', async ({ page }) => {
  await page.goto('/forgot-password');
  await expect(page.locator('#security-answer')).toBeVisible();
  await page.locator('#btn-reset').click();
  await expect(page.locator('#security-answer-error')).toBeVisible();
});

test('new password is required', async ({ page }) => {
  await page.goto('/forgot-password');
  await expect(page.locator('#new-password')).toBeVisible();
  await page.locator('#btn-reset').click();
  await expect(page.locator('#new-password-error')).toBeVisible();
});

test('password mismatch', async ({ page }) => {
  await page.goto('/forgot-password');
  await expect(page.locator('#new-password')).toBeVisible();
  await expect(page.locator('#verify-new-password')).toBeVisible();
  await page.locator('#new-password').fill('a');
  await page.locator('#verify-new-password').fill('b');
  await page.locator('#btn-reset').click();
  await expect(page.locator('#verify-new-password-error')).toBeVisible();
});

test('end to end forgot password', async ({ page }) => {
  const userName = uuidv4();
  const password = 'firstpassword';
  const newPassword = 'newPassword';
  const securityAnswer = 'my answer';

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
  await page.locator('#security-question-answer').fill(securityAnswer);
  await page.locator('#password').fill(password);
  await page.locator('#verify-password').fill(password);
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#btn-log-out')).toBeVisible();
  await page.locator('#btn-log-out').click();
  await expect(page).toHaveURL('/');
  await expect(page.getByRole('link', { name: 'Forgot password?' })).toBeVisible();
  await page.getByRole('link', { name: 'Forgot password?' }).click();
  await expect(page.locator('#user-name')).toBeVisible();
  await expect(page.locator('#security-answer')).toBeVisible();
  await expect(page.locator('#new-password')).toBeVisible();
  await expect(page.locator('#verify-new-password')).toBeVisible();
  await expect(page.locator('#btn-reset')).toBeVisible();
  await page.locator('#user-name').fill(userName);
  await page.locator('#security-answer').fill(securityAnswer);
  await page.locator('#new-password').fill(newPassword);
  await page.locator('#verify-new-password').fill(newPassword);
  await page.locator('#btn-reset').click();
  await expect(page.locator('#successful-reset')).toBeVisible();
  await page.getByRole('link', { name: /home/ }).click();
  await expect(page).toHaveURL('/');
  await page.locator('#user-name').fill(userName);
  await page.locator('#password').fill(newPassword);
  await page.locator('#login-button').click();
  await expect(page).toHaveURL('/');
  await expect(page.locator('#login-button')).not.toBeVisible();
  await expect(page.getByLabel('edit-goal').first()).toBeVisible();
  await expect(page.getByLabel('account settings')).toBeVisible();
  await page.getByLabel('account settings').click();
  await expect(page.locator('#btn-delete')).toBeVisible();
  await page.once('dialog', async (dialog) => {
    await dialog.accept();
  });
  await page.locator('#btn-delete').click();
  await expect(page).toHaveURL('/');
});
