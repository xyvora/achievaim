import { test, expect } from '@playwright/test';

test('end to end test', async ({ page }) => {
  await page.goto('http://localhost:3000/');

  // Test create user
  await page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }).click();
  await expect(page).toHaveURL('http://localhost:3000/signup');
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
  await page.locator('#verify-password').fill('mypassword');
  await page.locator('#btn-sign-up').click();

  // Wait for save to finish
  await expect(page).toHaveURL('http://localhost:3000/account-settings', { timeout: 10000 });
  await expect(page.locator('#btn-log-out')).toBeVisible();

  // Test log out
  await page.getByRole('button', { name: 'Log Out' }).click();
  await expect(page).toHaveURL('http://localhost:3000/');

  // Test log in
  await page.locator('#user-name').click();
  await page.locator('#user-name').fill('imma');
  await page.locator('#password').click();
  await page.locator('#password').fill('mypassword');
  await page.locator('#login-button').click();

  // Test user update
  await page.getByLabel('account-settings').click();
  await expect(page).toHaveURL('http://localhost:3000/account-settings');
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
  await expect(page).toHaveURL('http://localhost:3000/');

  // Test invalid user can't log in
  await page.locator('#user-name').click();
  await page.locator('#user-name').fill('imma');
  await page.locator('#password').click();
  await page.locator('#password').fill('mypassword');
  await page.locator('#login-button').click();
  await expect(page.locator('#generic-error')).toBeVisible();
});
