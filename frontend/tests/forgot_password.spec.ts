import { expect, test } from '@playwright/test';

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
