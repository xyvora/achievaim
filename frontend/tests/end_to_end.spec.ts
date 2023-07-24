import { test, expect } from '@playwright/test';

test('end to end test', async ({ page }) => {
  await page.goto('/');

  // Test create user
  await page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }).click();
  await expect(page).toHaveURL('/signup');

  // Test required fields
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#first-name-error')).toBeVisible();
  await expect(page.locator('#last-name-error')).toBeVisible();
  await expect(page.locator('#user-name-error')).toBeVisible();
  await expect(page.locator('#password-error')).toBeVisible();
  await expect(page.locator('#btn-sign-up')).toBeVisible();
  await expect(page.locator('#btn-save')).not.toBeVisible();
  await expect(page.locator('#btn-log-out')).not.toBeVisible();
  await expect(page.locator('#btn-delete')).not.toBeVisible();

  await page.locator('#first-name').click();
  await page.locator('#first-name').fill('Imma');
  await page.locator('#last-name').click();
  await page.locator('#last-name').fill('User');
  await page.locator('#user-name').click();
  await page.locator('#user-name').fill('imma');
  await page.locator('#country').click();
  await page.locator('#country').fill('USA');
  await page.locator('#password').click();
  await page.locator('#password').fill('mypassword');
  await page.locator('#verify-password').click();
  await page.locator('#verify-password').fill('bad');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#first-name-error')).not.toBeVisible();
  await expect(page.locator('#last-name-error')).not.toBeVisible();
  await expect(page.locator('#user-name-error')).not.toBeVisible();
  await expect(page.locator('password-error')).not.toBeVisible();
  await expect(page.locator('#password-verify-error')).toBeVisible();
  await page.locator('#verify-password').click();
  await page.locator('#verify-password').fill('mypassword');
  await page.locator('#btn-sign-up').click();

  // Wait for save to finish
  await expect(page).toHaveURL('/account-settings');
  await expect(page.locator('#btn-log-out')).toBeVisible();

  // Test log out
  await page.getByRole('button', { name: 'Log Out' }).click();
  await expect(page).toHaveURL('/');

  // Test log in
  await page.locator('#user-name').click();
  await page.locator('#user-name').fill('imma');
  await page.locator('#password').click();
  await page.locator('#password').fill('mypassword');
  await page.locator('#login-button').click();

  // Test user update
  await page.getByLabel('account-settings').click();
  await expect(page).toHaveURL('/account-settings');
  await page.locator('#country').click();
  await page.locator('#country').fill('Italy');
  await page.locator('#password').click();
  await page.locator('#password').fill('mypassword');
  await page.locator('#verify-password').click();
  await page.locator('#verify-password').fill('mypassword');
  await page.locator('#btn-save').click();
  await expect(page.locator('#country')).toHaveValue('Italy');

  // Test delete user
  await expect(page.locator('#btn-delete')).toBeVisible();
  page.once('dialog', async (dialog) => {
    await dialog.accept();
  });
  await page.locator('#btn-delete').click();
  await expect(page).toHaveURL('/');

  // Test invalid user can't log in
  await page.locator('#user-name').click();
  await page.locator('#user-name').fill('imma');
  await page.locator('#password').click();
  await page.locator('#password').fill('mypassword');
  await page.locator('#login-button').click();
  await expect(page.locator('#generic-error')).toBeVisible();
});
