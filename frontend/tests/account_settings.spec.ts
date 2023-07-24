import { expect, test } from '@playwright/test';

test('page loads', async ({ page }) => {
  await page.goto('/account-settings');
  await expect(page.locator('#navbar')).toBeVisible();
});

test('first name entered', async ({ page }) => {
  await page.goto('/account-settings');
  await page.locator('#first-name').fill('a');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#first-name-error')).not.toBeVisible();
});

test('first name required', async ({ page }) => {
  await page.goto('/account-settings');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#first-name-error')).toBeVisible();
});

test('last name entered', async ({ page }) => {
  await page.goto('/account-settings');
  await page.locator('#last-name').fill('a');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#last-name-error')).not.toBeVisible();
});

test('last name required', async ({ page }) => {
  await page.goto('/account-settings');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#last-name-error')).toBeVisible();
});

test('user name entered', async ({ page }) => {
  await page.goto('/account-settings');
  await page.locator('#user-name').fill('a');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#user-name-error')).not.toBeVisible();
});

test('user name required', async ({ page }) => {
  await page.goto('/account-settings');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#user-name-error')).toBeVisible();
});

test('password entered', async ({ page }) => {
  await page.goto('/account-settings');
  await page.locator('#password').fill('a');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('password-error')).not.toBeVisible();
});

test('password required', async ({ page }) => {
  await page.goto('/account-settings');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#password-error')).toBeVisible();
});

test('passwords match', async ({ page }) => {
  await page.goto('/account-settings');
  await page.locator('#password').fill('a');
  await page.locator('#verify-password').fill('a');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#password-verify-error')).not.toBeVisible();
});

test('passwords match error', async ({ page }) => {
  await page.goto('/account-settings');
  await page.locator('#password').fill('a');
  await page.locator('#verify-password').fill('b');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#password-verify-error')).toBeVisible();
});

test('not logged in buttons', async ({ page }) => {
  await page.goto('/account-settings');
  await expect(page.locator('#btn-sign-up')).toBeVisible();
  await expect(page.locator('#btn-save')).not.toBeVisible();
  await expect(page.locator('#btn-log-out')).not.toBeVisible();
  await expect(page.locator('#btn-delete')).not.toBeVisible();
});
